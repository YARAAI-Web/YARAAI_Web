rule auto_rule_20250726172513_9647 {
  strings:
    $o0 = "dword_472520" wide ascii nocase
    $o1 = "CodePagea" wide ascii nocase
  condition:
    all of them
}