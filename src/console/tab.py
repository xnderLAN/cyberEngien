tabs_in_mod = {

    "all_cmd" : [
        'add ',
        'show ',
        'help ',
        'exit ',
        'mode ',
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
        'target '
    ],
    "vul" : [
        'sqli ',
        'xxe ',
        'xss ',
        'ssrf ',
        'lfi ',
        'devulg '
    ],
    "show":{
        'search':{
            "field_names":['Variable', "required", "Discription"],
            "val":[
                ['vul','false','Specify a vulnerability to obtain precise results, for example: LFI, SQLI...'],
                ['dork','false','Specify the dork to use in the search.'],
                ['target','false','Specify the target in order to focus the search.']
                ]
            },

        'insert':{}
    }
}