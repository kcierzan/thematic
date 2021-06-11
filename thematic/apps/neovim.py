import os

import typer

from thematic import util
from thematic.apps import base
from thematic.constants import NVIM_SOCKET


class Neovim(base.App):
    supported_oses = {"darwin", "linux"}
    config_file = ".config/nvim/init.vim"
    theme_file = "theme.vim"
    # this should be a lua file of a table returning multiple values
    theme_template = """
local syntax = {
    Comment = { {{Comment}} };
    Constant = { {{Constant}} };
    Character = { {{Character}} };
    Conditional = { {{Conditional}} };
    Debug = { {{Debug}} } ;
    Define = { {{Define}} };
    Delimiter ={ {{Delimiter}} };
    Error = { {{Error}} };
    Exception = { {{Exception}} };
    Float = { {{Float}} };
    Function = { {{Function}} };
    Identifier = { {{Identifier}} };
    Ignore = { {{Ignore}} };
    Include = { {{Include}} };
    Keyword = { {{Keyword}} };
    Label = { {{Label}} };
    Macro = { {{Macro}} };
    Number = { {{Number}} };
    Operator = { {{}} };
    PreProc = { {{PreProc}} };
    PreCondit = { {{PreCondit}} };
    Repeat = { {{Repeat}} };
    Statement = { {{Statement}} };
    StorageClass = { {{StorageClass}} };
    Special = { {{Special}} };
    SpecialChar = { {{SpecialChar}} };
    Structure = { {{Structure}} };
    String = { {{String}} };
    SpecialComment = { {{SpecialComment}} };
    Typedef = { {{Typedef}} };
    Tag = { {{Tag}} };
    Type = { {{Type}} };
    Todo = { {{Todo}} };
    Underlined = { {{Underlined}} };
    TSError = { {{TSError}} };
    TSPunctDelimitter = { {{TSPunctDelimitter}} };
    TSPunctBracket = { {{TSPunctBracket}} };
    TSPunctSpecial = { {{TSPunctSpecial}} };
    TSConstant = { {{TSConstant}} };
    TSConstBuiltin = { {{TSConstBuiltin}} };
    TSContMacro = { {{TSContMacro}} };
    TSString = {  {{TSString}} };
    TSStringRegex = { {{TSStringRegex}} };
    TSCharacter = { {{TSCharacter}} };
    TSNumber = { {{TSNumber}} };
    TSBoolean = { {{TSBoolean}} };
    TSFloat = { {{TSFloat}} };
    TSAnnotation = { {{TSAnnotation}} };
    TSAttribute = { {{TSAttribute}} };
    TSNamespace = { {{TSNamespace}} };
    TSFunctionBuiltin = { {{TSFunctionBuiltin}} };
    TSFunction = { {{TSFunction}} };
    TSFuncMacro = { {{TSFuncMacro}} };
    TSParameter = { {{TSParameter}} };
    TSParameterReference = { {{TSParameterReference}} };
    TSMethod = { {{TSMethod}} };
    TSField = { {{TSField}} };
    TSProperty = {  {{TSProperty}} };
    TSConstructor = { {{TSConstructor}} };
    TSConditional = { {{TSConditional}} };
    TSRepeat = { {{TSRepeat}} };
    TSLabel = { {{TSLabel}} };
    TSKeyword = { {{TSKeyword}} };
    TSKeywordFunction = { {{TSKeywordFunction}} };
    TSKeywordOperator = { {{TSKeywordOperator}} };
    TSOperator = { {{TSOperator}} };
    TSExeption = { {{TSExeption}} };
    TSType = { {{TSType}} };
    TSTypeBuiltin = { {{TSTypeBuiltin}} };
    TSStructure = { {{TSStructure}} };
    TSInclude = { {{TSInclude}} };
    TSVariable = { {{TSVariable}} };
    TSVariableBuiltin = { {{TSVariableBuiltin}} };
    TSText = { {{TSText}} };
    TSStrong = { {{TSStrong}} };
    TSEmphasis = { {{TSEmphasis}} };
    TSUnderline = { {{TSUnderline}} };
    TSTitle = { {{TSTitle}} };
    TSLiteral = { {{TSLiteral}} };
    TSUri = { {{TSUri}} };
    TSTag = { {{TSTag}} };
    TSTagDelimitter = { {{TSTagDelimitter}} };
    BufferInactive = { {{BufferInactive}} };
    BufferInactiveTarge = { {{BufferInactiveTarge}} };
    BufferInactiveSign =  { {{BufferInactiveSign}} };
    BufferCurrent = { {{BufferCurrent}} };
    BufferCurrentSign = { {{BufferCurrentSign}} };
    BufferTabPageFill = { {{BufferTabPageFill}} };
    BufferCurrentMod = { {{BufferCurrentMod}} };
    BufferInactiveMod = { {{BufferInactiveMod}} };
    ColorColumn = { {{ColorColumn}} };
    Conceal = { {{Conceal}} };
    CursorLineNr = { {{CursorLineNr}} };
    CursorIM = { {{CursorIM}} };
    CursorColumn = { {{CursorColumn}} };
    CursorLine = { {{CursorLine}} };
    Cursor = { {{Cursor}} };
    DiffAdd = { {{DiffAdd}} };
    DiffChange = { {{DiffChange}} };
    DiffDelete = { {{DiffDelete}} };
    DiffText = { {{DiffText}} };
    Directory = { {{Directory}} };
    debugBreakpoint = { {{debugBreakpoint}} };
    EndOfBuffer = { {{EndOfBuffer}} };
    ErrorMsg = { {{ErrorMsg}} };
    FoldColumn = { {{FoldColumn}} };
    Folded = { {{Folded}} };
    iCursor =  { {{iCursor}} };
    IncSearch = { {{IncSearch}} };
    lCursor =   { {{lCursor}} };
    LineNr = { {{LineNr}} };
    ModeMsg = { {{ModeMsg}} };
    MatchParen = { {{MatchParen}} };
    Normal = { {{Normal}} };
    NormalFloat = { {{NormalFloat}} };
    NonText = { {{NonText}} };
    Pmenu = { {{Pmenu}} };
    PmenuSel = { {{PmenuSel}} };
    PmenuSelBold = { {{}} };
    PmenuSbar = { {{PmenuSbar}} };
    PmenuThumb = {  {{PmenuThumb}} };
    Question = { {{Question}} };
    QuickFixLine = { {{QuickFixLine}} };
    StatusLine = { {{StatusLine}} };
    StatusLineNC = { {{StatusLineNC}} };
    SpellBad = { {{SpellBad}} };
    SpellCap =   { {{SpellCap}} };
    SpellLocal = { {{SpellLocal}} };
    SpellRare =   { {{SpellRare}} };
    SignColumn = { {{SignColumn}} };
    Search = { {{Search}} };
    SpecialKey = { {{SpecialKey}} };
    TabLineSel = { {{TabLineSel}} };
    Title =  { {{Title}} };
    Terminal = { {{Terminal}} };
    TabLineFill =   { {{TabLineFill}} };
    VertSplit = { {{VertSplit}} };
    vCursor = { {{vCursor}} };
    WarningMsg =  { {{WarningMsg}} };
    Whitespace = { {{Whitespace}} };
    WildMenu =   { {{WildMenu}} };
    Visual = { {{Visual}} };
    VisualNOS = { {{VisualNOS}} }

}
local plugins = {

}
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
