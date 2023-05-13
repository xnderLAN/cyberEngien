tabs_in_mod = {

    "all_cmd" : [
        'add ',
        'show ',
        'help ',
        'exit ',
        'use ',
        'set ',
        'insert ',
        'search ',
        'vul ',
        'run ',
        'dork ',
        'del ',
        'back ',
        'sqli ',
        'xxe ',
        'xss ',
        'ssrf ',
        'lfi ',
        'devulg ',
        'target ',
        'flush ',
        'scop ',
        'option '
    ],
    "vul" : [
        'sqli ',
        'xxe ',
        'xss ',
        'ssrf ',
        'lfi ',
        'devulg '
    ],
    "option":{
        'search':{
            "field_names":['Variable','Value', "Required", "Discription"],
            "val":[
                ['vul',None,'false','Specify a vulnerability for example: LFI, SQLI...'],
                ['dork',None,'false','Specify the dork to use in the search.'],
                ['target',None,'false','Specify the target in order to focus the search.'],
                ['scop',10,'false','Specify the number of results you want per search']
                ]
            },

        'insert':{}
    }
}