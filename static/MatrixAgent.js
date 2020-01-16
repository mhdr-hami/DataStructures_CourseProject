function whatTheFaz(text)
{
    let txt = text.toLowerCase();
    //faz1
    if (txt.includes("faz") && (txt.includes("1") || txt.includes("one")))
    {
        return 1;
    }
    //faz2
    if (txt.includes("faz") && (txt.includes("2") || txt.includes("two")))
    {
        return 2;
    }
    //faz3
    if (txt.includes("faz") && (txt.includes("3") || txt.includes("three")))
    {
        return 3;
    }
    //faz4
    if (txt.includes("faz") && (txt.includes("4") || txt.includes("four")))
    {
        return 4;
    }
    //clear

    if (txt.includes("clear") || txt.includes("clr"))
    {
        if(!(txt.includes("right") || txt.includes("both")))
        {
            return -1;
        }
        if(txt.includes("right") && !txt.includes("left") && !txt.includes("both"))
        {
            return -2;
        }
        if((txt.includes("left") && txt.includes("right")) || txt.includes("both"))
        {
            return -3;
        }
    }
}