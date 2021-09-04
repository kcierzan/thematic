from typing import Union, Dict
from dataclasses import dataclass, field


@dataclass
class Xcolors:
    foreground: str
    background: str
    xcolors_00: str
    xcolors_01: str
    xcolors_02: str
    xcolors_03: str
    xcolors_04: str
    xcolors_05: str
    xcolors_06: str
    xcolors_07: str
    xcolors_08: str
    xcolors_09: str
    xcolors_10: str
    xcolors_11: str
    xcolors_12: str
    xcolors_13: str
    xcolors_14: str
    xcolors_15: str

@dataclass
class NeovimTheme:
    Boolean: Dict[str, str] = field(default_factory=dict)
    BufferCurrent: Dict[str, str] = field(default_factory=dict)
    BufferCurrentMod: Dict[str, str] = field(default_factory=dict)
    BufferCurrentSign: Dict[str, str] = field(default_factory=dict)
    BufferInactive: Dict[str, str] = field(default_factory=dict)
    BufferInactiveMod: Dict[str, str] = field(default_factory=dict)
    BufferInactiveSign: Dict[str, str] = field(default_factory=dict)
    BufferInactiveTarge: Dict[str, str] = field(default_factory=dict)
    BufferTabPageFill: Dict[str, str] = field(default_factory=dict)
    Character: Dict[str, str] = field(default_factory=dict)
    ColorColumn: Dict[str, str] = field(default_factory=dict)
    Comment: Dict[str, str] = field(default_factory=dict)
    Conceal: Dict[str, str] = field(default_factory=dict)
    Conditional: Dict[str, str] = field(default_factory=dict)
    Constant: Dict[str, str] = field(default_factory=dict)
    Cursor: Dict[str, str] = field(default_factory=dict)
    CursorColumn: Dict[str, str] = field(default_factory=dict)
    CursorIM: Dict[str, str] = field(default_factory=dict)
    CursorLine: Dict[str, str] = field(default_factory=dict)
    CursorLineNr: Dict[str, str] = field(default_factory=dict)
    Debug: Dict[str, str] = field(default_factory=dict)
    Define: Dict[str, str] = field(default_factory=dict)
    Delimiter: Dict[str, str] = field(default_factory=dict)
    DiffAdd: Dict[str, str] = field(default_factory=dict)
    DiffChange: Dict[str, str] = field(default_factory=dict)
    DiffDelete: Dict[str, str] = field(default_factory=dict)
    DiffText: Dict[str, str] = field(default_factory=dict)
    Directory: Dict[str, str] = field(default_factory=dict)
    EndOfBuffer: Dict[str, str] = field(default_factory=dict)
    Error: Dict[str, str] = field(default_factory=dict)
    ErrorMsg: Dict[str, str] = field(default_factory=dict)
    Exception: Dict[str, str] = field(default_factory=dict)
    Float: Dict[str, str] = field(default_factory=dict)
    FoldColumn: Dict[str, str] = field(default_factory=dict)
    Folded: Dict[str, str] = field(default_factory=dict)
    Function: Dict[str, str] = field(default_factory=dict)
    Identifier: Dict[str, str] = field(default_factory=dict)
    Ignore: Dict[str, str] = field(default_factory=dict)
    IncSearch: Dict[str, str] = field(default_factory=dict)
    Include: Dict[str, str] = field(default_factory=dict)
    Keyword: Dict[str, str] = field(default_factory=dict)
    Label: Dict[str, str] = field(default_factory=dict)
    LineNr: Dict[str, str] = field(default_factory=dict)
    Macro: Dict[str, str] = field(default_factory=dict)
    MatchParen: Dict[str, str] = field(default_factory=dict)
    ModeMsg: Dict[str, str] = field(default_factory=dict)
    NonText: Dict[str, str] = field(default_factory=dict)
    Normal: Dict[str, str] = field(default_factory=dict)
    NormalFloat: Dict[str, str] = field(default_factory=dict)
    Number: Dict[str, str] = field(default_factory=dict)
    Operator: Dict[str, str] = field(default_factory=dict)
    Pmenu: Dict[str, str] = field(default_factory=dict)
    PmenuSbar: Dict[str, str] = field(default_factory=dict)
    PmenuSel: Dict[str, str] = field(default_factory=dict)
    PmenuSelBold: Dict[str, str] = field(default_factory=dict)
    PmenuThumb: Dict[str, str] = field(default_factory=dict)
    PreCondit: Dict[str, str] = field(default_factory=dict)
    PreProc: Dict[str, str] = field(default_factory=dict)
    Question: Dict[str, str] = field(default_factory=dict)
    QuickFixLine: Dict[str, str] = field(default_factory=dict)
    Repeat: Dict[str, str] = field(default_factory=dict)
    Search: Dict[str, str] = field(default_factory=dict)
    SignColumn: Dict[str, str] = field(default_factory=dict)
    Special: Dict[str, str] = field(default_factory=dict)
    SpecialChar: Dict[str, str] = field(default_factory=dict)
    SpecialComment: Dict[str, str] = field(default_factory=dict)
    SpecialKey: Dict[str, str] = field(default_factory=dict)
    SpellBad: Dict[str, str] = field(default_factory=dict)
    SpellCap: Dict[str, str] = field(default_factory=dict)
    SpellLocal: Dict[str, str] = field(default_factory=dict)
    SpellRare: Dict[str, str] = field(default_factory=dict)
    Statement: Dict[str, str] = field(default_factory=dict)
    StatusLine: Dict[str, str] = field(default_factory=dict)
    StatusLineNC: Dict[str, str] = field(default_factory=dict)
    StorageClass: Dict[str, str] = field(default_factory=dict)
    String: Dict[str, str] = field(default_factory=dict)
    Structure: Dict[str, str] = field(default_factory=dict)
    TSAnnotation: Dict[str, str] = field(default_factory=dict)
    TSAttribute: Dict[str, str] = field(default_factory=dict)
    TSBoolean: Dict[str, str] = field(default_factory=dict)
    TSCharacter: Dict[str, str] = field(default_factory=dict)
    TSConditional: Dict[str, str] = field(default_factory=dict)
    TSConstBuiltin: Dict[str, str] = field(default_factory=dict)
    TSConstant: Dict[str, str] = field(default_factory=dict)
    TSConstructor: Dict[str, str] = field(default_factory=dict)
    TSContMacro: Dict[str, str] = field(default_factory=dict)
    TSEmphasis: Dict[str, str] = field(default_factory=dict)
    TSError: Dict[str, str] = field(default_factory=dict)
    TSException: Dict[str, str] = field(default_factory=dict)
    TSField: Dict[str, str] = field(default_factory=dict)
    TSFloat: Dict[str, str] = field(default_factory=dict)
    TSFuncMacro: Dict[str, str] = field(default_factory=dict)
    TSFunction: Dict[str, str] = field(default_factory=dict)
    TSFunctionBuiltin: Dict[str, str] = field(default_factory=dict)
    TSInclude: Dict[str, str] = field(default_factory=dict)
    TSKeyword: Dict[str, str] = field(default_factory=dict)
    TSKeywordFunction: Dict[str, str] = field(default_factory=dict)
    TSKeywordOperator: Dict[str, str] = field(default_factory=dict)
    TSLabel: Dict[str, str] = field(default_factory=dict)
    TSLiteral: Dict[str, str] = field(default_factory=dict)
    TSMath: Dict[str, str] = field(default_factory=dict)
    TSMethod: Dict[str, str] = field(default_factory=dict)
    TSNamespace: Dict[str, str] = field(default_factory=dict)
    TSNone: Dict[str, str] = field(default_factory=dict)
    TSNumber: Dict[str, str] = field(default_factory=dict)
    TSOperator: Dict[str, str] = field(default_factory=dict)
    TSParameter: Dict[str, str] = field(default_factory=dict)
    TSParameterReference: Dict[str, str] = field(default_factory=dict)
    TSProperty: Dict[str, str] = field(default_factory=dict)
    TSPunctBracket: Dict[str, str] = field(default_factory=dict)
    TSPunctDelimitter: Dict[str, str] = field(default_factory=dict)
    TSPunctSpecial: Dict[str, str] = field(default_factory=dict)
    TSRepeat: Dict[str, str] = field(default_factory=dict)
    TSStrike: Dict[str, str] = field(default_factory=dict)
    TSString: Dict[str, str] = field(default_factory=dict)
    TSStringRegex: Dict[str, str] = field(default_factory=dict)
    TSStrong: Dict[str, str] = field(default_factory=dict)
    TSStructure: Dict[str, str] = field(default_factory=dict)
    TSSymbol: Dict[str, str] = field(default_factory=dict)
    TSTag: Dict[str, str] = field(default_factory=dict)
    TSTagDelimitter: Dict[str, str] = field(default_factory=dict)
    TSText: Dict[str, str] = field(default_factory=dict)
    TSTitle: Dict[str, str] = field(default_factory=dict)
    TSType: Dict[str, str] = field(default_factory=dict)
    TSTypeBuiltin: Dict[str, str] = field(default_factory=dict)
    TSURI: Dict[str, str] = field(default_factory=dict)
    TSUnderline: Dict[str, str] = field(default_factory=dict)
    TSVariable: Dict[str, str] = field(default_factory=dict)
    TSVariableBuiltin: Dict[str, str] = field(default_factory=dict)
    TabLineFill: Dict[str, str] = field(default_factory=dict)
    TabLineSel: Dict[str, str] = field(default_factory=dict)
    Tag: Dict[str, str] = field(default_factory=dict)
    Terminal: Dict[str, str] = field(default_factory=dict)
    Title: Dict[str, str] = field(default_factory=dict)
    Todo: Dict[str, str] = field(default_factory=dict)
    Type: Dict[str, str] = field(default_factory=dict)
    Typedef: Dict[str, str] = field(default_factory=dict)
    Underlined: Dict[str, str] = field(default_factory=dict)
    VertSplit: Dict[str, str] = field(default_factory=dict)
    Visual: Dict[str, str] = field(default_factory=dict)
    VisualNOS: Dict[str, str] = field(default_factory=dict)
    WarningMsg: Dict[str, str] = field(default_factory=dict)
    Whitespace: Dict[str, str] = field(default_factory=dict)
    WildMenu: Dict[str, str] = field(default_factory=dict)
    debugBreakpoint: Dict[str, str] = field(default_factory=dict)
    iCursor: Dict[str, str] = field(default_factory=dict)
    lCursor: Dict[str, str] = field(default_factory=dict)
    vCursor: Dict[str, str] = field(default_factory=dict)
    qfFileName: Dict[str, str] = field(default_factory=dict)


@dataclass
class NeovimPluginTheme:
    DashboardCenter: Dict[str, str] = field(default_factory=dict)
    DashboardFooter: Dict[str, str] = field(default_factory=dict)
    DashboardHeader: Dict[str, str] = field(default_factory=dict)
    DashboardShortCut: Dict[str, str] = field(default_factory=dict)
    GitGutterAdd: Dict[str, str] = field(default_factory=dict)
    GitGutterChange: Dict[str, str] = field(default_factory=dict)
    GitGutterChangeDelete: Dict[str, str] = field(default_factory=dict)
    GitGutterDelete: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsError: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsInformation: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsSignError: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsSignInformation: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsSignWarning: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsSigndictnt: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsUnderlineError: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsUnderlineInformation: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsUnderlineWarning: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsUnderlinedictnt: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsVirtualTextError: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsVirtualTextInformation: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsVirtualTextWarning: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsVirtualTextdictnt: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsWarning: Dict[str, str] = field(default_factory=dict)
    LspDiagnosticsdictnt: Dict[str, str] = field(default_factory=dict)
    NvimTreeEmptyFolderName: Dict[str, str] = field(default_factory=dict)
    NvimTreeFolderIcon: Dict[str, str] = field(default_factory=dict)
    NvimTreeFolderName: Dict[str, str] = field(default_factory=dict)
    NvimTreeOpenedFolderName: Dict[str, str] = field(default_factory=dict)
    NvimTreeRootFolder: Dict[str, str] = field(default_factory=dict)
    NvimTreeSpecialFile: Dict[str, str] = field(default_factory=dict)
    SignifySignAdd: Dict[str, str] = field(default_factory=dict)
    SignifySignChange: Dict[str, str] = field(default_factory=dict)
    SignifySignDelete: Dict[str, str] = field(default_factory=dict)
    VistaChildrenNr: Dict[str, str] = field(default_factory=dict)
    VistaColon: Dict[str, str] = field(default_factory=dict)
    VistaIcon: Dict[str, str] = field(default_factory=dict)
    VistaKind: Dict[str, str] = field(default_factory=dict)
    VistaLineNr: Dict[str, str] = field(default_factory=dict)
    VistaPrefix: Dict[str, str] = field(default_factory=dict)
    VistaScope: Dict[str, str] = field(default_factory=dict)
    VistaScopeKind: Dict[str, str] = field(default_factory=dict)
    VistaTag: Dict[str, str] = field(default_factory=dict)
    Vistacyan: Dict[str, str] = field(default_factory=dict)
    WhichKey: Dict[str, str] = field(default_factory=dict)
    WhichKeyDesc: Dict[str, str] = field(default_factory=dict)
    WhichKeyFloat: Dict[str, str] = field(default_factory=dict)
    WhichKeyGroup: Dict[str, str] = field(default_factory=dict)
    WhichKeySeparator: Dict[str, str] = field(default_factory=dict)
    WhichKeySeperator: Dict[str, str] = field(default_factory=dict)
    WhichKeyValue: Dict[str, str] = field(default_factory=dict)
    cssAttrComma: Dict[str, str] = field(default_factory=dict)
    cssAttributeSelector: Dict[str, str] = field(default_factory=dict)
    cssBraces: Dict[str, str] = field(default_factory=dict)
    cssClassName: Dict[str, str] = field(default_factory=dict)
    cssClassNameDot: Dict[str, str] = field(default_factory=dict)
    cssDefinition: Dict[str, str] = field(default_factory=dict)
    cssFontAttr: Dict[str, str] = field(default_factory=dict)
    cssFontDescriptor: Dict[str, str] = field(default_factory=dict)
    cssFunctionName: Dict[str, str] = field(default_factory=dict)
    cssIdentifier: Dict[str, str] = field(default_factory=dict)
    cssImportant: Dict[str, str] = field(default_factory=dict)
    cssInclude: Dict[str, str] = field(default_factory=dict)
    cssIncludeKeyword: Dict[str, str] = field(default_factory=dict)
    cssMediaType: Dict[str, str] = field(default_factory=dict)
    cssProp: Dict[str, str] = field(default_factory=dict)
    cssPseudoClassId: Dict[str, str] = field(default_factory=dict)
    cssSelectorOp2: Dict[str, str] = field(default_factory=dict)
    cssSelectorOp: Dict[str, str] = field(default_factory=dict)
    cssTagName: Dict[str, str] = field(default_factory=dict)
    dbui_tables: Dict[str, str] = field(default_factory=dict)
    diffAdded: Dict[str, str] = field(default_factory=dict)
    diffChanged: Dict[str, str] = field(default_factory=dict)
    diffFile: Dict[str, str] = field(default_factory=dict)
    diffIndexLine: Dict[str, str] = field(default_factory=dict)
    diffLine: Dict[str, str] = field(default_factory=dict)
    diffNewFile: Dict[str, str] = field(default_factory=dict)
    diffOldFile: Dict[str, str] = field(default_factory=dict)
    diffRemoved: Dict[str, str] = field(default_factory=dict)
    gitcommitArrow: Dict[str, str] = field(default_factory=dict)
    gitcommitDiscarded: Dict[str, str] = field(default_factory=dict)
    gitcommitFile: Dict[str, str] = field(default_factory=dict)
    gitcommitOnBranch: Dict[str, str] = field(default_factory=dict)
    gitcommitSelected: Dict[str, str] = field(default_factory=dict)
    gitcommitSummary: Dict[str, str] = field(default_factory=dict)
    gitcommitUnmerged: Dict[str, str] = field(default_factory=dict)
    gitcommitUntracked: Dict[str, str] = field(default_factory=dict)
    goBuiltins: Dict[str, str] = field(default_factory=dict)
    goConst: Dict[str, str] = field(default_factory=dict)
    goDeclType: Dict[str, str] = field(default_factory=dict)
    goDeclaration: Dict[str, str] = field(default_factory=dict)
    goFunctionCall: Dict[str, str] = field(default_factory=dict)
    goType: Dict[str, str] = field(default_factory=dict)
    goTypeDecl: Dict[str, str] = field(default_factory=dict)
    goTypeName: Dict[str, str] = field(default_factory=dict)
    goVar: Dict[str, str] = field(default_factory=dict)
    goVarAssign: Dict[str, str] = field(default_factory=dict)
    goVarDefs: Dict[str, str] = field(default_factory=dict)
    javaScriptBraces: Dict[str, str] = field(default_factory=dict)
    javaScriptFunction: Dict[str, str] = field(default_factory=dict)
    javaScriptIdentifier: Dict[str, str] = field(default_factory=dict)
    javaScriptNull: Dict[str, str] = field(default_factory=dict)
    javaScriptNumber: Dict[str, str] = field(default_factory=dict)
    javaScriptRequire: Dict[str, str] = field(default_factory=dict)
    javaScriptReserved: Dict[str, str] = field(default_factory=dict)
    javascriptArrowFunc: Dict[str, str] = field(default_factory=dict)
    javascriptClassExtends: Dict[str, str] = field(default_factory=dict)
    javascriptClassKeyword: Dict[str, str] = field(default_factory=dict)
    javascriptDocNotation: Dict[str, str] = field(default_factory=dict)
    javascriptDocParamName: Dict[str, str] = field(default_factory=dict)
    javascriptDocTags: Dict[str, str] = field(default_factory=dict)
    javascriptEndColons: Dict[str, str] = field(default_factory=dict)
    javascriptExport: Dict[str, str] = field(default_factory=dict)
    javascriptFuncArg: Dict[str, str] = field(default_factory=dict)
    javascriptFuncKeyword: Dict[str, str] = field(default_factory=dict)
    javascriptIdentifier: Dict[str, str] = field(default_factory=dict)
    javascriptImport: Dict[str, str] = field(default_factory=dict)
    javascriptMethodName: Dict[str, str] = field(default_factory=dict)
    javascriptObjectLabel: Dict[str, str] = field(default_factory=dict)
    javascriptOpSymbol: Dict[str, str] = field(default_factory=dict)
    javascriptOpSymbols: Dict[str, str] = field(default_factory=dict)
    javascriptPropertyName: Dict[str, str] = field(default_factory=dict)
    javascriptTemplateSB: Dict[str, str] = field(default_factory=dict)
    javascriptVariable: Dict[str, str] = field(default_factory=dict)
    jsArrowFunction: Dict[str, str] = field(default_factory=dict)
    jsClassKeyword: Dict[str, str] = field(default_factory=dict)
    jsClassMethodType: Dict[str, str] = field(default_factory=dict)
    jsDocParam: Dict[str, str] = field(default_factory=dict)
    jsDocTags: Dict[str, str] = field(default_factory=dict)
    jsExport: Dict[str, str] = field(default_factory=dict)
    jsExportDefault: Dict[str, str] = field(default_factory=dict)
    jsExtendsKeyword: Dict[str, str] = field(default_factory=dict)
    jsFrom: Dict[str, str] = field(default_factory=dict)
    jsFuncCall: Dict[str, str] = field(default_factory=dict)
    jsFunction: Dict[str, str] = field(default_factory=dict)
    jsGenerator: Dict[str, str] = field(default_factory=dict)
    jsGlobalObjects: Dict[str, str] = field(default_factory=dict)
    jsImport: Dict[str, str] = field(default_factory=dict)
    jsModuleAs: Dict[str, str] = field(default_factory=dict)
    jsModuleWords: Dict[str, str] = field(default_factory=dict)
    jsModules: Dict[str, str] = field(default_factory=dict)
    jsNull: Dict[str, str] = field(default_factory=dict)
    jsOperator: Dict[str, str] = field(default_factory=dict)
    jsStorageClass: Dict[str, str] = field(default_factory=dict)
    jsSuper: Dict[str, str] = field(default_factory=dict)
    jsTemplateBraces: Dict[str, str] = field(default_factory=dict)
    jsTemplateVar: Dict[str, str] = field(default_factory=dict)
    jsThis: Dict[str, str] = field(default_factory=dict)
    jsUndefined: Dict[str, str] = field(default_factory=dict)
    vimCommand: Dict[str, str] = field(default_factory=dict)
    vimCommentTitle: Dict[str, str] = field(default_factory=dict)
    vimFuncName: Dict[str, str] = field(default_factory=dict)
    vimFunction: Dict[str, str] = field(default_factory=dict)
    vimIsCommand: Dict[str, str] = field(default_factory=dict)
    vimLet: Dict[str, str] = field(default_factory=dict)
    vimNotFunc: Dict[str, str] = field(default_factory=dict)
    vimUserFunc: Dict[str, str] = field(default_factory=dict)
    pythonExClass: Dict[str, str] = field(default_factory=dict)
    pythonBuiltinType: Dict[str, str] = field(default_factory=dict)
    pythonBuiltinObj: Dict[str, str] = field(default_factory=dict)
    pythonDottedName: Dict[str, str] = field(default_factory=dict)
    pythonBuiltinFunc: Dict[str, str] = field(default_factory=dict)
    pythonFunction: Dict[str, str] = field(default_factory=dict)
    pythonDecorator: Dict[str, str] = field(default_factory=dict)
    pythonInclude: Dict[str, str] = field(default_factory=dict)
    pythonImport: Dict[str, str] = field(default_factory=dict)
    pythonRun: Dict[str, str] = field(default_factory=dict)
    pythonCoding: Dict[str, str] = field(default_factory=dict)
    pythonOperator: Dict[str, str] = field(default_factory=dict)
    pythonConditional: Dict[str, str] = field(default_factory=dict)
    pythonRepeat: Dict[str, str] = field(default_factory=dict)
    pythonException: Dict[str, str] = field(default_factory=dict)
    pythonNone: Dict[str, str] = field(default_factory=dict)
    pythonDot: Dict[str, str] = field(default_factory=dict)
    pythonBuiltin: Dict[str, str] = field(default_factory=dict)
    pythonExceptions: Dict[str, str] = field(default_factory=dict)
    pythonDecoratorName: Dict[str, str] = field(default_factory=dict)
    CocUnusedHighlight: Dict[str, str] = field(default_factory=dict)

class Theme:
    name = ""
    autosuggestions = ""
    tmux_mode_fg = ""
    bg_bright = ""
    bg_brighter = ""
    bg_brightest = ""
    cursor = ""
    cursor_text = ""
    xcolors = Xcolors(
        foreground="",
        background="",
        xcolors_00="",
        xcolors_01="",
        xcolors_02="",
        xcolors_03="",
        xcolors_04="",
        xcolors_05="",
        xcolors_06="",
        xcolors_07="",
        xcolors_08="",
        xcolors_09="",
        xcolors_10="",
        xcolors_11="",
        xcolors_12="",
        xcolors_13="",
        xcolors_14="",
        xcolors_15=""
    )
    nvim_core = NeovimTheme()
    nvim_plugins = NeovimPluginTheme()

    @staticmethod
    def to_vim_highlights(vim_theme: Union[NeovimPluginTheme, NeovimTheme]) -> Dict[str, str]:
        vim_highlights = {}
        for key, value in vars(vim_theme).items():
            vim_highlights[key] = ", ".join("{} = '{}'".format(group, color) for group, color in value.items())
        return vim_highlights


    @classmethod
    def asdict(cls) -> Dict[str, str]:
        return {
            "name": cls.name,
            "autosuggestions": cls.autosuggestions,
            "tmux_mode_fg": cls.tmux_mode_fg,
            "bg_bright": cls.bg_bright,
            "bg_brighter": cls.bg_brighter,
            "bg_brightest": cls.bg_brightest,
            **vars(cls.xcolors),
            **cls.to_vim_highlights(cls.nvim_core),
            **cls.to_vim_highlights(cls.nvim_plugins)
        }


