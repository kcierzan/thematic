from thematic.themes import base


class Dracula(base.Theme):
    name = "dracula"

    foreground = "#f9f9f4"
    background = "#272936"
    bg_bright = "#313446"
    bg_brighter = "#474b64"
    bg_brightest = "#555a78"
    red = "#ff6d67"
    red_bright = "#473536"
    cyan = "#99ecfd"
    purple = "#c9a8fa"
    blue = "#7ad5f1"
    yellow = "#f3f89d"
    orange = "#ef9062"
    green = "#59f68d"
    black = "#2e3140"
    black_bright = "#1A181A"
    pink = "#ff92d0"
    white = "#c7c7c7"
    white_bright = "#feffff"

    autosuggestions = "238"
    tmux_mode_fg = green

    xcolors = base.Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=purple,
        xcolors_05=pink,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black_bright,
        xcolors_09=red_bright,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue,
        xcolors_13=orange,
        xcolors_14=cyan,
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
        CursorLineNr={"fg": green, "bg": bg_bright, "style": "bold"},
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
        Function={"fg": green},
        Identifier={"fg": cyan},
        IncSearch={"fg": bg_bright, "bg": yellow, "style": "NONE"},
        Include={"fg": purple},
        Keyword={"fg": pink},
        Label={"fg": yellow},
        LineNr={"fg": bg_brighter},
        Macro={"fg": yellow},
        MatchParen={"fg": orange, "bg": "NONE"},
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
        String={"fg": yellow},
        Structure={"fg": pink, "style": "italic"},
        TSAnnotation={"fg": purple},
        TSAttribute={"fg": yellow},
        TSBoolean={"fg": green},
        TSCharacter={"fg": green},
        TSConstBuiltin={"fg": cyan, "style": "italic"},
        TSConstant={"fg": pink, "style": "italic"},
        TSConstructor={"fg": foreground},
        TSFunction={"fg": green},
        TSFunctionBuiltin={"fg": green},
        TSInclude={"fg": purple},
        TSKeywordFunction={"fg": pink},
        TSKeywordOperator={"fg": pink},
        TSLabel={"fg": purple},
        TSMath={"fg": green},
        TSMethod={"fg": blue},
        TSNamespace={"fg": cyan},
        TSNumber={"fg": purple},
        TSParameter={"fg": orange, "style": "italic"},
        TSPunctDelimitter={"fg": bg_brighter},
        TSPunctSpecial={"fg": yellow},
        TSSymbol={"fg": yellow},
        TSText={"fg": green},
        TSType={"fg": yellow},
        TSTypeBuiltin={"fg": yellow},
        TSVariable={"fg": foreground},
        TSVariableBuiltin={"fg": cyan},
        TabLineFill={"style": "NONE"},
        TabLineSel={"bg": background},
        Tag={"fg": yellow},
        Terminal={"fg": foreground, "bg": background},
        Title={"fg": purple, "style": "bold"},
        Todo={"fg": yellow, "style": "italic"},
        Type={"fg": cyan, "style": "italic"},
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
    nvim_plugins = base.NeovimPluginTheme(
        NvimTreeFolderName={"fg": foreground},
        NvimTreeEmptyFolderName={"fg": bg_brighter},
        NvimTreeOpenedFolderName={"fg": foreground},
    )
