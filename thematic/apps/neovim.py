import os

import typer

from thematic import util
from thematic.apps import base
from thematic.constants import NVIM_SOCKET


class Neovim(base.App):
    supported_oses = {"darwin", "linux"}
    config_file = ".config/nvim/init.vim"
    theme_file = "nvim-theme.lua"
    # this should be a lua file of a table returning multiple values
    theme_template = """
local syntax = {
    BufferCurrent = { {{BufferCurrent}} };
    BufferCurrentMod = { {{BufferCurrentMod}} };
    BufferCurrentSign = { {{BufferCurrentSign}} };
    BufferInactive = { {{BufferInactive}} };
    BufferInactiveMod = { {{BufferInactiveMod}} };
    BufferInactiveSign =  { {{BufferInactiveSign}} };
    BufferInactiveTarge = { {{BufferInactiveTarge}} };
    BufferTabPageFill = { {{BufferTabPageFill}} };
    Character = { {{Character}} };
    ColorColumn = { {{ColorColumn}} };
    Comment = { {{Comment}} };
    Conceal = { {{Conceal}} };
    Conditional = { {{Conditional}} };
    Constant = { {{Constant}} };
    Cursor = { {{Cursor}} };
    CursorColumn = { {{CursorColumn}} };
    CursorIM = { {{CursorIM}} };
    CursorLine = { {{CursorLine}} };
    CursorLineNr = { {{CursorLineNr}} };
    Debug = { {{Debug}} } ;
    Define = { {{Define}} };
    Delimiter ={ {{Delimiter}} };
    DiffAdd = { {{DiffAdd}} };
    DiffChange = { {{DiffChange}} };
    DiffDelete = { {{DiffDelete}} };
    DiffText = { {{DiffText}} };
    Directory = { {{Directory}} };
    EndOfBuffer = { {{EndOfBuffer}} };
    Error = { {{Error}} };
    ErrorMsg = { {{ErrorMsg}} };
    Exception = { {{Exception}} };
    Float = { {{Float}} };
    FoldColumn = { {{FoldColumn}} };
    Folded = { {{Folded}} };
    Function = { {{Function}} };
    Identifier = { {{Identifier}} };
    Ignore = { {{Ignore}} };
    IncSearch = { {{IncSearch}} };
    Include = { {{Include}} };
    Keyword = { {{Keyword}} };
    Label = { {{Label}} };
    LineNr = { {{LineNr}} };
    Macro = { {{Macro}} };
    MatchParen = { {{MatchParen}} };
    ModeMsg = { {{ModeMsg}} };
    NonText = { {{NonText}} };
    Normal = { {{Normal}} };
    NormalFloat = { {{NormalFloat}} };
    Number = { {{Number}} };
    Operator = { {{Operator}} };
    Pmenu = { {{Pmenu}} };
    PmenuSbar = { {{PmenuSbar}} };
    PmenuSel = { {{PmenuSel}} };
    PmenuSelBold = { {{PmenuSelBold}} };
    PmenuThumb = {  {{PmenuThumb}} };
    PreCondit = { {{PreCondit}} };
    PreProc = { {{PreProc}} };
    Question = { {{Question}} };
    QuickFixLine = { {{QuickFixLine}} };
    Repeat = { {{Repeat}} };
    Search = { {{Search}} };
    SignColumn = { {{SignColumn}} };
    Special = { {{Special}} };
    SpecialChar = { {{SpecialChar}} };
    SpecialComment = { {{SpecialComment}} };
    SpecialKey = { {{SpecialKey}} };
    SpellBad = { {{SpellBad}} };
    SpellCap =   { {{SpellCap}} };
    SpellLocal = { {{SpellLocal}} };
    SpellRare =   { {{SpellRare}} };
    Statement = { {{Statement}} };
    StatusLine = { {{StatusLine}} };
    StatusLineNC = { {{StatusLineNC}} };
    StorageClass = { {{StorageClass}} };
    String = { {{String}} };
    Structure = { {{Structure}} };
    TSAnnotation = { {{TSAnnotation}} };
    TSAttribute = { {{TSAttribute}} };
    TSBoolean = { {{TSBoolean}} };
    TSCharacter = { {{TSCharacter}} };
    TSConditional = { {{TSConditional}} };
    TSConstBuiltin = { {{TSConstBuiltin}} };
    TSConstant = { {{TSConstant}} };
    TSConstructor = { {{TSConstructor}} };
    TSContMacro = { {{TSContMacro}} };
    TSEmphasis = { {{TSEmphasis}} };
    TSError = { {{TSError}} };
    TSExeption = { {{TSExeption}} };
    TSField = { {{TSField}} };
    TSFloat = { {{TSFloat}} };
    TSNone = { {{TSNone}} };
    TSFuncMacro = { {{TSFuncMacro}} };
    TSFunction = { {{TSFunction}} };
    TSFunctionBuiltin = { {{TSFunctionBuiltin}} };
    TSInclude = { {{TSInclude}} };
    TSKeyword = { {{TSKeyword}} };
    TSKeywordFunction = { {{TSKeywordFunction}} };
    TSKeywordOperator = { {{TSKeywordOperator}} };
    TSLabel = { {{TSLabel}} };
    TSLiteral = { {{TSLiteral}} };
    TSMath = { {{TSMath}} };
    TSMethod = { {{TSMethod}} };
    TSNamespace = { {{TSNamespace}} };
    TSNumber = { {{TSNumber}} };
    TSOperator = { {{TSOperator}} };
    TSParameter = { {{TSParameter}} };
    TSParameterReference = { {{TSParameterReference}} };
    TSProperty = {  {{TSProperty}} };
    TSPunctBracket = { {{TSPunctBracket}} };
    TSPunctDelimitter = { {{TSPunctDelimitter}} };
    TSPunctSpecial = { {{TSPunctSpecial}} };
    TSRepeat = { {{TSRepeat}} };
    TSStrike = { {{TSStrike}} };
    TSString = {  {{TSString}} };
    TSStringRegex = { {{TSStringRegex}} };
    TSStrong = { {{TSStrong}} };
    TSStructure = { {{TSStructure}} };
    TSSymbol = { {{TSSymbol}} };
    TSTag = { {{TSTag}} };
    TSTagDelimitter = { {{TSTagDelimitter}} };
    TSText = { {{TSText}} };
    TSTitle = { {{TSTitle}} };
    TSType = { {{TSType}} };
    TSTypeBuiltin = { {{TSTypeBuiltin}} };
    TSURI = { {{TSURI}} };
    TSURI = { {{TSURI}} };
    TSUnderline = { {{TSUnderline}} };
    TSVariable = { {{TSVariable}} };
    TSVariableBuiltin = { {{TSVariableBuiltin}} };
    TabLineFill =   { {{TabLineFill}} };
    TabLineSel = { {{TabLineSel}} };
    Tag = { {{Tag}} };
    Terminal = { {{Terminal}} };
    Title =  { {{Title}} };
    Todo = { {{Todo}} };
    Type = { {{Type}} };
    Typedef = { {{Typedef}} };
    Underlined = { {{Underlined}} };
    VertSplit = { {{VertSplit}} };
    Visual = { {{Visual}} };
    VisualNOS = { {{VisualNOS}} };
    WarningMsg =  { {{WarningMsg}} };
    Whitespace = { {{Whitespace}} };
    WildMenu =   { {{WildMenu}} };
    debugBreakpoint = { {{debugBreakpoint}} };
    iCursor =  { {{iCursor}} };
    lCursor =   { {{lCursor}} };
    vCursor = { {{vCursor}} };
}
local plugins = {
    DashboardCenter = { {{DashboardCenter}} };
    DashboardFooter = { {{DashboardFooter}} };
    DashboardHeader = { {{DashboardHeader}} };
    DashboardShortCut = { {{DashboardShortCut}} };
    GitGutterAdd = { {{GitGutterAdd}} };
    GitGutterChange = { {{GitGutterChange}} };
    GitGutterChangeDelete = { {{GitGutterChangeDelete}} };
    GitGutterDelete = { {{GitGutterDelete}} };
    LspDiagnosticsError = { {{LspDiagnosticsError}} };
    LspDiagnosticsInformation = { {{LspDiagnosticsInformation}} };
    LspDiagnosticsSignError = { {{LspDiagnosticsSignError}} };
    LspDiagnosticsSignInformation = { {{LspDiagnosticsSignInformation}} };
    LspDiagnosticsSignWarning = { {{LspDiagnosticsSignWarning}} };
    LspDiagnosticsSigndictnt = { {{LspDiagnosticsSigndictnt}} };
    LspDiagnosticsUnderlineError = { {{LspDiagnosticsUnderlineError}} };
    LspDiagnosticsUnderlineInformation = { {{LspDiagnosticsUnderlineInformation}} };
    LspDiagnosticsUnderlineWarning = { {{LspDiagnosticsUnderlineWarning}} };
    LspDiagnosticsUnderlinedictnt = { {{LspDiagnosticsUnderlinedictnt}} };
    LspDiagnosticsVirtualTextError = { {{LspDiagnosticsVirtualTextError}} };
    LspDiagnosticsVirtualTextInformation = { {{LspDiagnosticsVirtualTextInformation}} };
    LspDiagnosticsVirtualTextWarning = { {{LspDiagnosticsVirtualTextWarning}} };
    LspDiagnosticsVirtualTextdictnt = { {{LspDiagnosticsVirtualTextdictnt}} };
    LspDiagnosticsWarning = { {{LspDiagnosticsWarning}} };
    LspDiagnosticsdictnt = { {{LspDiagnosticsdictnt}} };
    NvimTreeEmptyFolderName = { {{NvimTreeEmptyFolderName}} };
    NvimTreeFolderIcon = { {{NvimTreeFolderIcon}} };
    NvimTreeFolderName = { {{NvimTreeFolderName}} };
    NvimTreeOpenedFolderName = { {{NvimTreeOpenedFolderName}} };
    NvimTreeRootFolder = { {{NvimTreeRootFolder}} };
    NvimTreeSpecialFile = { {{NvimTreeSpecialFile}} };
    SignifySignAdd = { {{SignifySignAdd}} };
    SignifySignChange = { {{SignifySignChange}} };
    SignifySignDelete = { {{SignifySignDelete}} };
    VistaChildrenNr = { {{VistaChildrenNr}} };
    VistaColon = { {{VistaColon}} };
    VistaIcon = { {{VistaIcon}} };
    VistaKind = { {{VistaKind}} };
    VistaLineNr = { {{VistaLineNr}} };
    VistaPrefix = { {{VistaPrefix}} };
    VistaScope = { {{VistaScope}} };
    VistaScopeKind = { {{VistaScopeKind}} };
    VistaTag = { {{VistaTag}} };
    Vistacyan = { {{Vistacyan}} };
    WhichKey = { {{WhichKey}} };
    WhichKeyDesc = { {{WhichKeyDesc}} };
    WhichKeyFloat = { {{WhichKeyFloat}} };
    WhichKeyGroup = { {{WhichKeyGroup}} };
    WhichKeySeparator = { {{WhichKeySeparator}} };
    WhichKeyValue = { {{WhichKeyValue}} };
    cssAttrComma = { {{cssAttrComma}} };
    cssAttributeSelector = { {{cssAttributeSelector}} };
    cssBraces = { {{cssBraces}} };
    cssClassName = { {{cssClassName}} };
    cssClassNameDot = { {{cssClassNameDot}} };
    cssDefinition = { {{cssDefinition}} };
    cssFontAttr = { {{cssFontAttr}} };
    cssFontDescriptor = { {{cssFontDescriptor}} };
    cssFunctionName = { {{cssFunctionName}} };
    cssIdentifier = { {{cssIdentifier}} };
    cssImportant = { {{cssImportant}} };
    cssInclude = { {{cssInclude}} };
    cssIncludeKeyword = { {{cssIncludeKeyword}} };
    cssMediaType = { {{cssMediaType}} };
    cssProp = { {{cssProp}} };
    cssPseudoClassId = { {{cssPseudoClassId}} };
    cssSelectorOp2 = { {{cssSelectorOp}} };
    cssSelectorOp = { {{cssSelectorOp}} };
    cssTagName = { {{cssTagName}} };
    dbui_tables = { {{dbui_tables}} };
    diffAdded = { {{diffAdded}} };
    diffChanged = { {{diffChanged}} };
    diffFile = { {{diffFile}} };
    diffIndexLine = { {{diffIndexLine}} };
    diffLine = { {{diffLine}} };
    diffNewFile = { {{diffNewFile}} };
    diffOldFile = { {{diffOldFile}} };
    diffRemoved = { {{diffRemoved}} };
    gitcommitArrow = { {{gitcommitArrow}} };
    gitcommitDiscarded = { {{gitcommitDiscarded}} };
    gitcommitFile = { {{gitcommitFile}} };
    gitcommitOnBranch = { {{gitcommitOnBranch}} };
    gitcommitSelected = { {{gitcommitSelected}} };
    gitcommitSummary = { {{gitcommitSummary}} };
    gitcommitUnmerged = { {{gitcommitUnmerged}} };
    gitcommitUntracked = { {{gitcommitUntracked}} };
    goBuiltins = { {{goBuiltins}} };
    goConst = { {{goConst}} };
    goDeclType = { {{goDeclType}} };
    goDeclaration = { {{goDeclaration}} };
    goFunctionCall = { {{goFunctionCall}} };
    goType = { {{goType}} };
    goTypeDecl = { {{goTypeDecl}} };
    goTypeName = { {{goTypeName}} };
    goVar = { {{goVar}} };
    goVarAssign = { {{goVarAssign}} };
    goVarDefs = { {{goVarDefs}} };
    javaScriptBraces = { {{javaScriptBraces}} };
    javaScriptFunction = { {{javaScriptFunction}} };
    javaScriptIdentifier = { {{javaScriptIdentifier}} };
    javaScriptNull = { {{javaScriptNull}} };
    javaScriptNumber = { {{javaScriptNumber}} };
    javaScriptRequire = { {{javaScriptRequire}} };
    javaScriptReserved = { {{javaScriptReserved}} };
    javascriptArrowFunc = { {{javascriptArrowFunc}} };
    javascriptClassExtends = { {{javascriptClassExtends}} };
    javascriptClassKeyword = { {{javascriptClassKeyword}} };
    javascriptDocNotation = { {{javascriptDocNotation}} };
    javascriptDocParamName = { {{javascriptDocParamName}} };
    javascriptDocTags = { {{javascriptDocTags}} };
    javascriptEndColons = { {{javascriptEndColons}} };
    javascriptExport = { {{javascriptExport}} };
    javascriptFuncArg = { {{javascriptFuncArg}} };
    javascriptFuncKeyword = { {{javascriptFuncKeyword}} };
    javascriptIdentifier = { {{javascriptIdentifier}} };
    javascriptImport = { {{javascriptImport}} };
    javascriptMethodName = { {{javascriptMethodName}} };
    javascriptObjectLabel = { {{javascriptObjectLabel}} };
    javascriptOpSymbol = { {{javascriptOpSymbol}} };
    javascriptOpSymbols = { {{javascriptOpSymbols}} };
    javascriptPropertyName = { {{javascriptPropertyName}} };
    javascriptTemplateSB = { {{javascriptTemplateSB}} };
    javascriptVariable = { {{javascriptVariable}} };
    jsArrowFunction = { {{jsArrowFunction}} };
    jsClassKeyword = { {{jsClassKeyword}} };
    jsClassMethodType = { {{jsClassMethodType}} };
    jsDocParam = { {{jsDocParam}} };
    jsDocTags = { {{jsDocTags}} };
    jsExport = { {{jsExport}} };
    jsExportDefault = { {{jsExportDefault}} };
    jsExtendsKeyword = { {{jsExtendsKeyword}} };
    jsFrom = { {{jsFrom}} };
    jsFuncCall = { {{jsFuncCall}} };
    jsFunction = { {{jsFunction}} };
    jsGenerator = { {{jsGenerator}} };
    jsGlobalObjects = { {{jsGlobalObjects}} };
    jsImport = { {{jsImport}} };
    jsModuleAs = { {{jsModuleAs}} };
    jsModuleWords = { {{jsModuleWords}} };
    jsModules = { {{jsModules}} };
    jsNull = { {{jsNull}} };
    jsOperator = { {{jsOperator}} };
    jsStorageClass = { {{jsStorageClass}} };
    jsSuper = { {{jsSuper}} };
    jsTemplateBraces = { {{jsTemplateBraces}} };
    jsTemplateVar = { {{jsTemplateVar}} };
    jsThis = { {{jsThis}} };
    jsUndefined = { {{jsUndefined}} };
    vimCommand = { {{vimCommand}} };
    vimCommentTitle = { {{vimCommentTitle}} };
    vimFuncName = { {{vimFuncName}} };
    vimFunction = { {{vimFunction}} };
    vimIsCommand = { {{vimIsCommand}} };
    vimLet = { {{vimLet}} };
    vimNotFunc = { {{vimNotFunc}} };
    vimUserFunc = { {{vimUserFunc}} };
    pythonExClass = { {{pythonExClass}} };
    pythonBuiltinType = { {{pythonBuiltinType}} };
    pythonBuiltinObj = { {{pythonBuiltinObj}} };
    pythonDottedName = { {{pythonDottedName}} };
    pythonBuiltinFunc = { {{pythonBuiltinFunc}} };
    pythonFunction = { {{pythonFunction}} };
    pythonDecorator = { {{pythonDecorator}} };
    pythonInclude = { {{pythonInclude}} };
    pythonImport = { {{pythonImport}} };
    pythonRun = { {{pythonRun}} };
    pythonCoding = { {{pythonCoding}} };
    pythonOperator = { {{pythonOperator}} };
    pythonConditional = { {{pythonConditional}} };
    pythonRepeat = { {{pythonRepeat}} };
    pythonException = { {{pythonException}} };
    pythonNone = { {{pythonNone}} };
    pythonDot = { {{pythonDot}} };
    pythonBuiltin = { {{pythonBuiltin}} };
    pythonExceptions = { {{pythonExceptions}} };
    pythonDecoratorName = { {{pythonDecoratorName}} };
}
return syntax, plugins
    """

    @staticmethod
    async def set_theme(theme: str) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    # TODO: fix the reloading of lua plugins
    @staticmethod
    async def reload() -> None:
        if not os.environ.get(NVIM_SOCKET):
            typer.echo(f"${NVIM_SOCKET} env var not set! Neovim will not be reloaded.")
            return

        nvim_socket = os.environ.get(NVIM_SOCKET)

        if nvim_socket and os.path.exists(nvim_socket):
            command = "nvr --nostart --remote-send ':so ~/.config/nvim/init.vim<CR>'"
            await util.call_with_shell(command)
