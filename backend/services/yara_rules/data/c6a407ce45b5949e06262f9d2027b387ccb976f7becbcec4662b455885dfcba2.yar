rule auto_rule_20250726102459_0333 {
  strings:
    $o0 = "dword_4624AC" wide ascii nocase
    $o1 = "dword_462CAC" wide ascii nocase
  condition:
    all of them
}