rule auto_rule_20250727031344_8295 {
  strings:
    $o0 = "_fcloseall" wide ascii nocase
    $o1 = "dword_460604" wide ascii nocase
    $o2 = "dword_45FE30" wide ascii nocase
  condition:
    3 of ($o*)
}