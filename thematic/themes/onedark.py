from thematic.themes import base


class Onedark(base.Theme):
    name = "onedark"
    foreground = "#B2BED1"
    background = "#2c2e34"
    bg_bright = "#303339"
    bg_brighter = "#42444e"
    bg_brightest = "#4d4f5b"

    black = "#393f4a"
    red = "#ec7279"
    green = "#a0c980"
    yellow = "#deb974"
    blue = "#6cb6eb"
    purple = "#d38aea"
    cyan = "#5dbbc1"
    cyan_bright = "#4db5bd"
    white = "#b9bfc9"
    black_bright = "#6f7683"
    red_bright = "#c9665b"
    green_bright = "#62ac65"
    yellow_bright = "#d9a97c"
    blue_bright = "#71bdf2"
    purple_bright = "#a9a1e1"
    white_bright = "#afb0b5"

    autosuggestions = "238"
    tmux_mode_fg = blue

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
        xcolors_09=red_bright,
        xcolors_10=green_bright,
        xcolors_11=yellow_bright,
        xcolors_12=blue_bright,
        xcolors_13=purple_bright,
        xcolors_14=cyan_bright,
        xcolors_15=white_bright,
    )
    nvim_core = base.NeovimTheme(
        Boolean={"fg": green},
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
        Comment={"fg": black_bright, "style": "italic"},
        Conceal={"fg": bg_bright, "bg": "NONE"},
        Conditional={"fg": purple},
        Constant={"fg": yellow, "style": "italic"},
        Cursor={"fg": "NONE", "bg": "NONE", "style": "reverse"},
        CursorColumn={"fg": "NONE", "bg": black_bright},
        CursorIM={"fg": "NONE", "bg": "NONE", "style": "reverse"},
        CursorLine={"fg": "NONE", "bg": bg_bright},
        CursorLineNr={"fg": blue, "bg": bg_bright, "style": "bold"},
        Define={"fg": purple},
        DiffAdd={"fg": background, "bg": green},
        DiffChange={"fg": background, "bg": yellow},
        DiffDelete={"fg": background, "bg": red},
        DiffText={"fg": background, "bg": foreground},
        Directory={"fg": bg_bright, "bg": "NONE"},
        EndOfBuffer={"fg": background, "bg": "NONE"},
        Error={"fg": red},
        ErrorMsg={"fg": red, "bg": "NONE", "style": "bold"},
        Exception={"fg": purple},
        Float={"fg": green},
        FoldColumn={"fg": foreground, "bg": background},
        Folded={"fg": bg_bright, "bg": bg_bright},
        Function={"fg": blue},
        Identifier={"fg": cyan},
        IncSearch={"fg": bg_bright, "bg": yellow, "style": "NONE"},
        Include={"fg": purple},
        Keyword={"fg": purple},
        Label={"fg": yellow},
        LineNr={"fg": black_bright},
        Macro={"fg": yellow},
        MatchParen={"fg": red, "bg": "NONE"},
        ModeMsg={"fg": foreground, "bg": "NONE", "style": "bold"},
        NonText={"fg": bg_bright},
        NormalFloat={"fg": foreground, "bg": bg_bright},
        Number={"fg": green},
        Operator={"fg": purple},
        Pmenu={"fg": foreground, "bg": bg_bright},
        PmenuSbar={"fg": "NONE", "bg": bg_bright},
        PmenuSel={"fg": bg_bright, "bg": blue},
        PmenuSelBold={"fg": bg_bright, "g": blue},
        PmenuThumb={"fg": purple, "bg": green},
        PreCondit={"fg": purple},
        PreProc={"fg": purple},
        Question={"fg": yellow},
        QuickFixLine={"fg": purple, "style": "bold"},
        Repeat={"fg": purple},
        Search={"fg": background, "bg": yellow},
        Special={"fg": blue},
        SpecialChar={"fg": yellow},
        SpecialComment={"fg": bg_bright},
        SpecialKey={"fg": bg_bright},
        SpellBad={"fg": red, "bg": "NONE", "style": "undercurl"},
        SpellCap={"fg": "bue", "bg": "NONE", "style": "undercurl"},
        SpellLocal={"fg": cyan, "bg": "NONE", "style": "undercurl"},
        SpellRare={"fg": purple, "bg": "NONE", "style": "undercurl"},
        Statement={"fg": purple},
        StatusLine={"fg": bg_bright, "bg": bg_brighter, "style": "NONE"},
        StatusLineNC={"fg": bg_bright, "bg": bg_bright, "style": "NONE"},
        StorageClass={"fg": red, "style": "italic"},
        String={"fg": green},
        Structure={"fg": red, "style": "italic"},
        TSAnnotation={"fg": purple},
        TSAttribute={"fg": yellow},
        TSBoolean={"fg": green},
        TSCharacter={"fg": green},
        TSConstBuiltin={"fg": cyan, "style": "italic"},
        TSConstant={"fg": red, "style": "italic"},
        TSConstructor={"fg": foreground},
        TSFunction={"fg": blue},
        TSFunctionBuiltin={"fg": blue},
        TSInclude={"fg": purple},
        TSKeywordFunction={"fg": purple},
        TSKeywordOperator={"fg": purple},
        TSLabel={"fg": purple},
        TSMath={"fg": green},
        TSMethod={"fg": blue},
        TSNamespace={"fg": yellow},
        TSNumber={"fg": yellow},
        TSParameter={"fg": red, "style": "italic"},
        TSPunctDelimitter={"fg": bg_brighter},
        TSPunctSpecial={"fg": yellow},
        TSSymbol={"fg": yellow},
        TSText={"fg": green},
        TSType={"fg": yellow},
        TSTypeBuiltin={"fg": yellow},
        TSVariable={"fg": red},
        TSVariableBuiltin={"fg": cyan},
        TabLineFill={"style": "NONE"},
        TabLineSel={"bg": background},
        Tag={"fg": yellow},
        Terminal={"fg": foreground, "bg": background},
        Title={"fg": purple, "style": "bold"},
        Todo={"fg": yellow, "style": "italic"},
        Type={"fg": red, "style": "italic"},
        Typedef={"fg": purple},
        Underlined={"style": "underline"},
        VertSplit={"fg": background},
        Visual={"fg": "NONE", "bg": bg_brighter},
        VisualNOS={"fg": background, "bg": foreground, "style": "underline"},
        WarningMsg={"fg": yellow, "bg": "NONE", "style": "bold"},
        Whitespace={"fg": bg_bright},
        WildMenu={"fg": foreground, "bg": green},
        debugBreakpoint={"fg": background, "bg": red},
        iCursor={"fg": bg_bright, "bg": "NONE", "style": "reverse"},
        lCursor={"fg": "NONE", "bg": "NONE", "style": "reverse"},
        vCursor={"fg": "NONE", "bg": "NONE", "style": "reverse"},
    )
    nvim_plugins = base.NeovimPluginTheme()
