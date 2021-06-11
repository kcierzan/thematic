from typing import Union
from dataclasses import dataclass


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
    Comment: dict = {}
    Constant: dict = {}
    Character: dict = {}
    Conditional: dict = {}
    Debug: dict = {}
    Define: dict = {}
    Delimiter: dict = {}
    Error: dict = {}
    Exception: dict = {}
    Float: dict = {}
    Function: dict = {}
    Identifier: dict = {}
    Ignore: dict = {}
    Include: dict = {}
    Keyword: dict = {}
    Label: dict = {}
    Macro: dict = {}
    Number: dict = {}
    Operator: dict = {}
    PreProc: dict = {}
    PreCondit: dict = {}
    Repeat: dict = {}
    Statement: dict = {}
    StorageClass: dict = {}
    Special: dict = {}
    SpecialChar: dict = {}
    Structure: dict = {}
    String: dict = {}
    SpecialComment: dict = {}
    Typedef: dict = {}
    Tag: dict = {}
    Type: dict = {}
    Todo: dict = {}
    Underlined: dict = {}
    TSError: dict = {}
    TSPunctDelimitter: dict = {}
    TSPunctBracket: dict = {}
    TSPunctSpecial: dict = {}
    TSConstant: dict = {}
    TSConstBuiltin: dict = {}
    TSContMacro: dict = {}
    TSString: dict = {}
    TSStringRegex: dict = {}
    TSCharacter: dict = {}
    TSNumber: dict = {}
    TSBoolean: dict = {}
    TSFloat: dict = {}
    TSAnnotation: dict = {}
    TSAttribute: dict = {}
    TSNamespace: dict = {}
    TSFunctionBuiltin: dict = {}
    TSFunction: dict = {}
    TSFuncMacro: dict = {}
    TSParameter: dict = {}
    TSParameterReference: dict = {}
    TSMethod: dict = {}
    TSField: dict = {}
    TSProperty: dict = {}
    TSConstructor: dict = {}
    TSConditional: dict = {}
    TSRepeat: dict = {}
    TSLabel: dict = {}
    TSKeyword: dict = {}
    TSKeywordFunction: dict = {}
    TSKeywordOperator: dict = {}
    TSOperator: dict = {}
    TSExeption: dict = {}
    TSType: dict = {}
    TSTypeBuiltin: dict = {}
    TSStructure: dict = {}
    TSInclude: dict = {}
    TSVariable: dict = {}
    TSVariableBuiltin: dict = {}
    TSText: dict = {}
    TSStrong: dict = {}
    TSEmphasis: dict = {}
    TSUnderline: dict = {}
    TSTitle: dict = {}
    TSLiteral: dict = {}
    TSUri: dict = {}
    TSTag: dict = {}
    TSTagDelimitter: dict = {}
    BufferInactive: dict = {}
    BufferInactiveTarge: dict = {}
    BufferInactiveSign: dict = {}
    BufferCurrent: dict = {}
    BufferCurrentSign: dict = {}
    BufferTabPageFill: dict = {}
    BufferCurrentMod: dict = {}
    BufferInactiveMod: dict = {}
    ColorColumn: dict = {}
    Conceal: dict = {}
    CursorLineNr: dict = {}
    CursorIM: dict = {}
    CursorColumn: dict = {}
    CursorLine: dict = {}
    Cursor: dict = {}
    DiffAdd: dict = {}
    DiffChange: dict = {}
    DiffDelete: dict = {}
    DiffText: dict = {}
    Directory: dict = {}
    debugBreakpoint: dict = {}
    EndOfBuffer: dict = {}
    ErrorMsg: dict = {}
    FoldColumn: dict = {}
    Folded: dict = {}
    iCursor: dict = {}
    IncSearch: dict = {}
    lCursor: dict = {}
    LineNr: dict = {}
    ModeMsg: dict = {}
    MatchParen: dict = {}
    Normal: dict = {}
    NormalFloat: dict = {}
    NonText: dict = {}
    Pmenu: dict = {}
    PmenuSel: dict = {}
    PmenuSelBold: dict = {}
    PmenuSbar: dict = {}
    PmenuThumb: dict = {}
    Question: dict = {}
    QuickFixLine: dict = {}
    StatusLine: dict = {}
    StatusLineNC: dict = {}
    SpellBad: dict = {}
    SpellCap: dict = {}
    SpellLocal: dict = {}
    SpellRare: dict = {}
    SignColumn: dict = {}
    Search: dict = {}
    SpecialKey: dict = {}
    TabLineSel: dict = {}
    Title: dict = {}
    Terminal: dict = {}
    TabLineFill: dict = {}
    VertSplit: dict = {}
    vCursor: dict = {}
    WarningMsg: dict = {}
    Whitespace: dict = {}
    WildMenu: dict = {}
    Visual: dict = {}
    VisualNOS: dict = {}


@dataclass
class NeovimPluginTheme:
    cssAttrComma: dict = {}
    cssAttributeSelector: dict = {}
    cssBraces: dict = {}
    cssClassName: dict = {}
    cssClassNameDot: dict = {}
    cssDefinition: dict = {}
    cssFontAttr: dict = {}
    cssFontDescriptor: dict = {}
    cssFunctionName: dict = {}
    cssIdentifier: dict = {}
    cssImportant: dict = {}
    cssInclude: dict = {}
    cssIncludeKeyword: dict = {}
    cssMediaType: dict = {}
    cssProp: dict = {}
    cssPseudoClassId: dict = {}
    cssSelectorOp: dict = {}
    cssSelectorOp2: dict = {}
    cssTagName: dict = {}
    goDeclaration: dict = {}
    goBuiltins: dict = {}
    goFunctionCall: dict = {}
    goVarDefs: dict = {}
    goVarAssign: dict = {}
    goVar: dict = {}
    goConst: dict = {}
    goType: dict = {}
    goTypeName: dict = {}
    goDeclType: dict = {}
    goTypeDecl: dict = {}
    javaScriptBraces: dict = {}
    javaScriptFunction: dict = {}
    javaScriptIdentifier: dict = {}
    javaScriptNull: dict = {}
    javaScriptNumber: dict = {}
    javaScriptRequire: dict = {}
    javaScriptReserved: dict = {}
    jsArrowFunction: dict = {}
    jsClassKeyword: dict = {}
    jsClassMethodType: dict = {}
    jsDocParam: dict = {}
    jsDocTags: dict = {}
    jsExport: dict = {}
    jsExportDefault: dict = {}
    jsExtendsKeyword: dict = {}
    jsFrom: dict = {}
    jsFuncCall: dict = {}
    jsFunction: dict = {}
    jsGenerator: dict = {}
    jsGlobalObjects: dict = {}
    jsImport: dict = {}
    jsModuleAs: dict = {}
    jsModuleWords: dict = {}
    jsModules: dict = {}
    jsNull: dict = {}
    jsOperator: dict = {}
    jsStorageClass: dict = {}
    jsSuper: dict = {}
    jsTemplateBraces: dict = {}
    jsTemplateVar: dict = {}
    jsThis: dict = {}
    jsUndefined: dict = {}
    javascriptArrowFunc: dict = {}
    javascriptClassExtends: dict = {}
    javascriptClassKeyword: dict = {}
    javascriptDocNotation: dict = {}
    javascriptDocParamName: dict = {}
    javascriptDocTags: dict = {}
    javascriptEndColons: dict = {}
    javascriptExport: dict = {}
    javascriptFuncArg: dict = {}
    javascriptFuncKeyword: dict = {}
    javascriptIdentifier: dict = {}
    javascriptImport: dict = {}
    javascriptMethodName: dict = {}
    javascriptObjectLabel: dict = {}
    javascriptOpSymbol: dict = {}
    javascriptOpSymbols: dict = {}
    javascriptPropertyName: dict = {}
    javascriptTemplateSB: dict = {}
    javascriptVariable: dict = {}
    vimCommentTitle: dict = {}
    vimLet: dict = {}
    vimVar: dict = {}
    vimFunction: dict = {}
    vimIsCommand: dict = {}
    vimCommand: dict = {}
    vimNotFunc: dict = {}
    vimUserFunc: dict = {}
    vimFuncName: dict = {}
    GitGutterAdd: dict = {}
    GitGutterChange: dict = {}
    GitGutterDelete: dict = {}
    GitGutterChangeDelete: dict = {}
    diffAdded: dict = {}
    diffRemoved: dict = {}
    diffChanged: dict = {}
    diffOldFile: dict = {}
    diffNewFile: dict = {}
    diffFile: dict = {}
    diffLine: dict = {}
    diffIndexLine: dict = {}
    gitcommitSummary: dict = {}
    gitcommitUntracked: dict = {}
    gitcommitDiscarded: dict = {}
    gitcommitSelected: dict = {}
    gitcommitUnmerged: dict = {}
    gitcommitOnBranch: dict = {}
    gitcommitArrow: dict = {}
    gitcommitFile: dict = {}
    Vistacyan: dict = {}
    VistaChildrenNr: dict = {}
    VistaKind: dict = {}
    VistaScope: dict = {}
    VistaScopeKind: dict = {}
    VistaTag: dict = {}
    VistaPrefix: dict = {}
    VistaColon: dict = {}
    VistaIcon: dict = {}
    VistaLineNr: dict = {}
    SignifySignAdd: dict = {}
    SignifySignChange: dict = {}
    SignifySignDelete: dict = {}
    dbui_tables: dict = {}
    DashboardShortCut: dict = {}
    DashboardHeader: dict = {}
    DashboardCenter: dict = {}
    DashboardFooter: dict = {}
    LspDiagnosticsError: dict = {}
    LspDiagnosticsWarning: dict = {}
    LspDiagnosticsInformation: dict = {}
    LspDiagnosticsdictnt: dict = {}
    LspDiagnosticsSignError: dict = {}
    LspDiagnosticsSignWarning: dict = {}
    LspDiagnosticsSignInformation: dict = {}
    LspDiagnosticsSigndictnt: dict = {}
    LspDiagnosticsVirtualTextError: dict = {}
    LspDiagnosticsVirtualTextWarning: dict = {}
    LspDiagnosticsVirtualTextInformation: dict = {}
    LspDiagnosticsVirtualTextdictnt: dict = {}
    LspDiagnosticsUnderlineError: dict = {}
    LspDiagnosticsUnderlineWarning: dict = {}
    LspDiagnosticsUnderlineInformation: dict = {}
    LspDiagnosticsUnderlinedictnt: dict = {}
    NvimTreeEmptyFolderName: dict = {}
    NvimTreeOpenedFolderName: dict = {}
    NvimTreeFolderName: dict = {}
    NvimTreeRootFolder: dict = {}
    NvimTreeSpecialFile: dict = {}
    NvimTreeFolderIcon: dict = {}
    WhichKey: dict = {}
    WhichKeyGroup: dict = {}
    WhichKeyDesc: dict = {}
    WhichKeySeperator: dict = {}
    WhichKeySeparator: dict = {}
    WhichKeyFloat: dict = {}
    WhichKeyValue: dict = {}

class Theme:
    name = ""
    autosuggestions = ""
    bat_theme = ""
    tmux_mode_fg = ""
    bg_bright = ""
    bg_brighter = ""
    bg_brightest = ""
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
    def to_vim_highlights(vim_theme: Union[NeovimPluginTheme, NeovimTheme]) -> "dict[str, str]":
        vim_highlights = {}
        for key, value in vars(vim_theme):
            vim_highlights[key] = ",".join("{} = '{}'".format(group, color) for group, color in value.items())
        return vim_highlights


    @classmethod
    def asdict(cls) -> dict:
        return {
            "name": cls.name,
            "autosuggestions": cls.autosuggestions,
            "bat_theme": cls.bat_theme,
            "tmux_mode_fg": cls.tmux_mode_fg,
            "bg_bright": cls.bg_bright,
            "bg_brighter": cls.bg_brighter,
            "bg_brightest": cls.bg_brightest,
            **vars(cls.xcolors),
            **cls.to_vim_highlights(cls.nvim_core),
            **cls.to_vim_highlights(cls.nvim_plugins)
        }


