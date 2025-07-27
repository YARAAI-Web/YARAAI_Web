rule auto_rule_20250727014328_8846 {
  strings:
    $o0 = "dword_43D020" wide ascii nocase
    $o1 = "dword_468580" wide ascii nocase
  condition:
    all of them
}