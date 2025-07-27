rule auto_rule_20250727015302_6649 {
  strings:
    $o0 = "byte_40F208" wide ascii nocase
    $o1 = "dword_40EAC0" wide ascii nocase
    $o2 = "_c_exit" wide ascii nocase
  condition:
    3 of ($o*)
}