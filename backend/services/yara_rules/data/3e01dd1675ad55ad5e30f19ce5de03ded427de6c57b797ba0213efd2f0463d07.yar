rule auto_rule_20250726113608_6563 {
  strings:
    $o0 = "grfFlags" wide ascii nocase
    $o1 = "hRgn" wide ascii nocase
    $o2 = "GetAsyncKeyState" wide ascii nocase
  condition:
    3 of ($o*)
}