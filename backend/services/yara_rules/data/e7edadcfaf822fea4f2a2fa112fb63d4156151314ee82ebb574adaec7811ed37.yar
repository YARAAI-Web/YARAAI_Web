rule auto_rule_20250726155158_2067 {
  strings:
    $o0 = "hWndInsertAfter" wide ascii nocase
    $o1 = "wvsprintfA" wide ascii nocase
    $o2 = "xF89C853F" wide ascii nocase
    $o3 = "x57CCu" wide ascii nocase
  condition:
    4 of ($o*)
}