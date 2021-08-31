from thematic.themes import base


class GruvboxDark(base.Theme):
    name = "gruvbox-dark"

    foreground = "#ddc7a1"
    background = "#282828"
    bg_bright = "#32302f"
    bg_brighter = "#3c3836"
    bg_brightest = "#45403d"
    red = "#ea6962"
    cyan = "#89b482"
    blue = "#7daea3"
    yellow = "#d8a657"
    orange = "#e78a4e"
    green = "#a9b665"
    black = "#46413e"
    black_bright = "#5b534d"
    purple = "#d3869b"
    white = "#d4be98"
    white_bright = "#a89984"

    autosuggestions = "238"
    tmux_mode_fg = orange

    xcolors = base.Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=blue,
        xcolors_05=purple,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black_bright,
        xcolors_09=red,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white_bright,
    )
    nvim_core = base.NeovimTheme(
        Boolean={"fg": purple},
        BufferCurrent={"fg": yellow, "bg": background, "style": "bold"},
        BufferCurrentMod={"fg": blue, "bg": background},
        BufferCurrentSign={"fg": blue, "bg": background},
        BufferInactive={"fg": foreground, "bg": bg_bright},
        BufferInactiveMod={"fg": blue, "bg": bg_bright},
        BufferInactiveSign={"fg": blue, "bg": bg_bright},
        BufferInactiveTarge={"fg": foreground, "bg": bg_bright},
        BufferTabPageFill={"fg": blue, "bg": background},
        Character={"fg": green},
        ColorColumn={"fg": "NONE", "bg": bg_bright},
        Comment={"fg": black_bright},
        Conceal={"fg": bg_brighter, "bg": "NONE"},
        Conditional={"fg": red, "style": "italic"},
        Constant={"fg": cyan},
        Cursor={"fg": "NONE", "bg": "NONE", "style": "reverse"},
        CursorColumn={"fg": "NONE", "bg": black_bright},
        CursorIM={"fg": "NONE", "bg": "NONE", "style": "reverse"},
        CursorLine={"fg": "NONE", "bg": bg_bright},
        CursorLineNr={"fg": yellow, "bg": bg_bright},
        Define={"fg": purple, "style": "italic"},
        DiffAdd={"fg": background, "bg": green},
        DiffChange={"fg": background, "bg": yellow},
        DiffDelete={"fg": background, "bg": red},
        DiffText={"fg": background, "bg": foreground},
        Directory={"fg": bg_bright, "bg": "NONE"},
        EndOfBuffer={"fg": background, "bg": "NONE"},
        Error={"fg": red},
        ErrorMsg={"fg": red, "bg": "NONE", "style": "bold"},
        Exception={"fg": red},
        Float={"fg": purple},
        FoldColumn={"fg": foreground, "bg": background},
        Folded={"fg": bg_bright, "bg": bg_bright},
        Function={"fg": yellow, "style": "bold"},
        Identifier={"fg": blue},
        IncSearch={"fg": bg_bright, "bg": yellow, "style": "NONE"},
        Include={"fg": purple, "style": "italic"},
        Keyword={"fg": purple, "style": "italic"},
        Label={"fg": purple},
        LineNr={"fg": black_bright},
        Macro={"fg": purple},
        MatchParen={"fg": red, "bg": "NONE"},
        ModeMsg={"fg": foreground, "bg": "NONE", "style": "bold"},
        NonText={"fg": bg_bright},
        NormalFloat={"fg": foreground, "bg": bg_bright},
        Number={"fg": purple},
        Operator={"fg": orange},
        Pmenu={"fg": foreground, "bg": bg_bright},
        PmenuSbar={"fg": "NONE", "bg": bg_bright},
        PmenuSel={"fg": bg_bright, "bg": blue},
        PmenuSelBold={"fg": bg_bright, "g": blue},
        PmenuThumb={"fg": purple, "bg": green},
        PreCondit={"fg": purple, "style": "italic"},
        PreProc={"fg": purple, "style": "italic"},
        Question={"fg": yellow},
        QuickFixLine={"fg": purple, "style": "bold"},
        Repeat={"fg": red, "style": "italic"},
        Search={"fg": background, "bg": yellow},
        Special={"fg": yellow},
        SpecialChar={"fg": yellow},
        SpecialComment={"fg": black_bright},
        SpecialKey={"fg": bg_bright},
        SpellBad={"fg": red, "bg": "NONE", "style": "undercurl"},
        SpellCap={"fg": "bue", "bg": "NONE", "style": "undercurl"},
        SpellLocal={"fg": cyan, "bg": "NONE", "style": "undercurl"},
        SpellRare={"fg": purple, "bg": "NONE", "style": "undercurl"},
        Statement={"fg": red, "style": "italic"},
        StatusLine={"fg": bg_bright, "bg": bg_brighter, "style": "NONE"},
        StatusLineNC={"fg": bg_bright, "bg": bg_bright, "style": "NONE"},
        StorageClass={"fg": orange},
        String={"fg": green},
        Structure={"fg": orange},
        TSAttribute={"fg": purple},
        TSConstructor={"fg": foreground},
        TSConstant={"fg": purple},
        TSFunction={"fg": yellow},
        TSInclude={"fg": red},
        TSKeywordFunction={"fg": cyan},
        TSKeywordOperator={"fg": orange},
        TSLabel={"fg": orange},
        TSNumber={"fg": purple},
        TSOperator={"fg": yellow},
        TSException={"fg": red},
        TSProperty={"fg": purple},
        TSString={"fg": green},
        TSTag={"fg": orange},
        TSVariable={"fg": foreground},
        TSVariableBuiltin={"fg": blue},
        TabLineFill={"style": "NONE"},
        TabLineSel={"bg": background},
        Terminal={"fg": foreground, "bg": background},
        Tag={"fg": orange},
        Title={"fg": orange, "style": "bold"},
        Todo={"fg": purple},
        Type={"fg": orange},
        Typedef={"fg": red, "style": "italic"},
        Underlined={"style": "underline"},
        VertSplit={"fg": background},
        Visual={"fg": "NONE", "bg": bg_bright},
        VisualNOS={"fg": background, "bg": foreground},
        WarningMsg={"fg": yellow, "bg": "NONE", "style": "bold"},
        Whitespace={"fg": bg_bright},
        WildMenu={"fg": foreground, "bg": green},
        debugBreakpoint={"fg": background, "bg": red},
        iCursor={"fg": bg_bright, "bg": "NONE", "style": "reverse"},
        lCursor={"fg": "NONE", "bg": "NONE", "style": "reverse"},
        vCursor={"fg": "NONE", "bg": "NONE", "style": "reverse"},
    )
    nvim_plugins = base.NeovimPluginTheme(
        NvimTreeFolderName={"fg": foreground},
        NvimTreeEmptyFolderName={"fg": bg_brighter},
        NvimTreeOpenedFolderName={"fg": foreground},
    )
