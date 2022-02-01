Function Log10(ByVal x As Double) As Double

    Log10 = Log(x) / Log(10)
    
End Function

Function Racine_2(ByVal n As Integer) As Integer

    Dim a As Long, b As Long, c As Long, d As Long
    Dim i As Integer
    
    a = 1
    b = 1
    c = 1
    d = 1
    
    If n = 0 Then
        Racine_2 = 0
    Else
        For i = 1 To n
            a = c + 2 * d
            b = c + d
            c = a
            d = b
        Next
    End If
    Debug.Print a
    Debug.Print b
    Racine_2 = Int(Log10(a)) - Int(Log10(b))
End Function

Sub test()

    Dim i As Integer
    Dim s As Double
    
    For i = 2 To 10000
        s = s + Racine_2(i)
    Next
    Debug.Print s
End Sub
