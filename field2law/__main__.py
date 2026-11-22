import argparse
import json
from pathlib import Path
from . import DEFAULT_ROOT, catalog, load_task, verify, export_task


def main():
    parser=argparse.ArgumentParser(description='Field2Law public observations and modeling tasks')
    parser.add_argument('--root',type=Path,default=DEFAULT_ROOT)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('list')
    inspect=sub.add_parser('inspect');inspect.add_argument('task');inspect.add_argument('--panel',choices=['main','noise'],default='main')
    check=sub.add_parser('verify');check.add_argument('--require-external',action='store_true')
    export=sub.add_parser('export');export.add_argument('task');export.add_argument('destination',type=Path)
    export.add_argument('--panel',choices=['main','noise'],default='main');export.add_argument('--conditions',action='store_true')
    fetch=sub.add_parser('fetch-external');fetch.add_argument('source',choices=['pc3','waves']);fetch.add_argument('--source-file',type=Path)
    args=parser.parse_args()
    if args.command=='list':
        for t in catalog(args.root)['tasks']:print(f"{t['panel']:5s} {t['difficulty']} {t['id']:35s} {t['title']}")
    elif args.command=='inspect':
        doc,arrays=load_task(args.task,args.panel,args.root)
        print(json.dumps({'task':doc,'arrays':{k:{'shape':list(v.shape),'dtype':str(v.dtype)} for k,v in arrays.items()}},ensure_ascii=False,indent=2))
    elif args.command=='verify':
        result=verify(args.root,args.require_external);print(json.dumps(result,indent=2))
        raise SystemExit(0 if result['ok'] else 1)
    elif args.command=='export':
        print(export_task(args.task,args.destination,args.panel,args.conditions,args.root))
    else:
        from .external import acquire
        print(json.dumps(acquire(args.source,args.source_file,args.root),indent=2))


if __name__=='__main__':main()
