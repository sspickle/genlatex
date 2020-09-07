#!/usr/bin/env python

import argparse
import jinja2
import os
import math
import random
import importlib.util
import sys

def createTeXs(latex_jinja_env,
               path, seeds, args,
               data = None,
               answers = None,
               templateFile = None,
               quizFilenameTemplate = None,
               quizSolnFilenameTemplate = None):
               
    outQuizTemplate = os.path.sep.join([path, quizFilenameTemplate])
    outSolnTemplate = os.path.sep.join([path, quizSolnFilenameTemplate])
    template = latex_jinja_env.get_template(os.path.join(path,templateFile))

    digits = math.ceil(math.log(max(seeds)+1,10)) # zfill digits

    for i in range(len(data)):
        cnt = str(seeds[i]).zfill(digits)
        
        if data and not args.ans:
            texPromptSource = template.render(data = data[i])
            f = open(outQuizTemplate.format(cnt),'w')
            f.write(texPromptSource)
            f.close()

        if answers and not args.prompt:
            texSolnSource = template.render(data=data[i], ans=answers[i])
            f = open(outSolnTemplate.format(cnt),'w')
            f.write(texSolnSource)
            f.close()

def main():
    parser = argparse.ArgumentParser( description="Generate LateX Files from a template and a python helper",
                                    epilog="and that's how you'd generate some LaTeX files.")

    parser.add_argument('file_path')
    parser.add_argument('--seed','-s', nargs='+',default=None, type=int, help='seed value(s)')
    parser.add_argument('--num','-n',action='store', default=1, type=int, help='number of outputs')
    parser.add_argument('--ans', '-a', action='store_true', help='answer only mode')
    parser.add_argument('--prompt', '-p', action='store_true', help='prompt only mode')
    parser.add_argument('--debug', '-d', action='store_true', help='debug mode on')
    parser.add_argument('--srcdir', '-r', help='force source dir to be this')

    args = parser.parse_args()

    if args.debug:
        import pdb
        pdb.set_trace()

    def seedFunc(i, seeds=None):
        return seeds and (seeds[i:] and seeds[i:][0] or (seeds[-1]+(i-len(seeds)+1))) or i 
        
    seeds = [seedFunc(i, args.seed) for i in range(args.num)] # get seeds

    # For illustrative purposes.
    file_path = args.file_path
    path,fname = os.path.split(file_path)
    module_name, ext = os.path.splitext(fname)

    if args.srcdir:
        #
        # when running in a container, the user will map /app/src to their cwd. Need to fix this up
        # to find the module correctly in the mapped drive
        #

        path = (path and os.path.join(args.srcdir,path)) or args.srcdir
        file_path = os.path.join(path, fname)
    elif not path:
        path = '.'

    if ext != '.py':
        print("Only python files can be imported.")
        sys.exit(-1)

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    latex_jinja_env = jinja2.Environment(
        block_start_string = r'\BLOCK{',
        block_end_string = '}',
        variable_start_string = r'\VAR{',
        variable_end_string = '}',
        comment_start_string = r'\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader = jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    createTeXs(latex_jinja_env, path, seeds, args, **module.getTemplateValues(args.num, seeds))

if __name__ == '__main__':
    main()
