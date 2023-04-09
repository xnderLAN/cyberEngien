help = """
Usage: mode [mode]

Available modes:
  mod             Switch between insert and search modes
  insert          Enter the mode for adding new dorks to the database
  search          Enter the mode for searching for dorks

Examples:
  mode insert      Enter the mode for inserting new dorks
  mode search      Enter the mode for searching for dorks

Usage: [Search] Doks >> set <name> <value>

Set the value of a configuration option.

Options:
  vul        Set the value of the vulnerability option
  dork       Set the value of the dork option

Examples:
  app-console set vul SQLInjection    Set the value of the vulnerability option to SQLInjection
  app-console set dork "inurl:index.php?id="  Set the value of the dork option to "inurl:index.php?id="


"""