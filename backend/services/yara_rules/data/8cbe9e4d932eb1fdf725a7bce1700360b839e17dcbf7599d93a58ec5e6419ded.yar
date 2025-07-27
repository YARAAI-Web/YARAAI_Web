rule auto_rule_20250726150224_8185 {
  strings:
    $o0 = "x89B" wide ascii nocase
    $o1 = "dword_42B004" wide ascii nocase
    $o2 = "dword_42B008" wide ascii nocase
  condition:
    3 of ($o*)
}