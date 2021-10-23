//Program to demonstrate the New keyword in C#

using System;

class Sample1
{
    public void Method()
    {
        Console.WriteLine("Sample1.Method() called");
    }
}

class Sample2
{
    public void Method()
    {
        Console.WriteLine("Sample2.Method() called");
    }
}

class NewDemo
{
    static void Main()
    {
        Sample1 S1 = new Sample1();
        Sample2 S2 = new Sample2();

        S1.Method();
        S2.Method();
    }
}
