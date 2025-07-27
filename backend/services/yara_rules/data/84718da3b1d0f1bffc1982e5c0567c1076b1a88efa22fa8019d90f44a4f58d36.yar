rule auto_rule_20250726215802_2745 {
  strings:
    $o0 = "dword_42E813" wide ascii nocase
    $o1 = "xF89C8532" wide ascii nocase
  condition:
    all of them
}