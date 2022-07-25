(async ({}) => {
                
    const {default: HighlightedCode} =
        await import('https://unpkg.com/highlighted-code');
    
    HighlightedCode.useTheme('monokai-sublime'); // Themes --> https://github.com/highlightjs/highlight.js/tree/main/src/styles
    })(self);
