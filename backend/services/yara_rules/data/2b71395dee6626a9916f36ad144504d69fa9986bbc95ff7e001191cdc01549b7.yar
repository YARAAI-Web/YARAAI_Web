rule auto_rule_20250726102308_5461 {
  strings:
    $o0 = "GetWindowTextLengthW" wide ascii nocase
    $o1 = "dword_42A884" wide ascii nocase
  condition:
    all of them
}