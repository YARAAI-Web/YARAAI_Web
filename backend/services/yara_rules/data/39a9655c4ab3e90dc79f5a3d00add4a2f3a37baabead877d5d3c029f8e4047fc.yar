rule auto_rule_20250726233456_7317 {
  strings:
    $o0 = "ev184Jz9P6O3xZCldE7" wide ascii nocase
    $o1 = "dword_409868" wide ascii nocase
    $o2 = "ObVwyCa9gMPonLEh" wide ascii nocase
    $o3 = "x3F7D6400" wide ascii nocase
  condition:
    4 of ($o*)
}