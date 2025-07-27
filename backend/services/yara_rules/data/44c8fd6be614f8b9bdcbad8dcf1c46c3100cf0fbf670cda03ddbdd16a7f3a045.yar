rule auto_rule_20250726064339_3853 {
  strings:
    $o0 = "dword_42FD75" wide ascii nocase
    $o1 = "NewItem" wide ascii nocase
    $o2 = "dword_42E198" wide ascii nocase
  condition:
    3 of ($o*)
}