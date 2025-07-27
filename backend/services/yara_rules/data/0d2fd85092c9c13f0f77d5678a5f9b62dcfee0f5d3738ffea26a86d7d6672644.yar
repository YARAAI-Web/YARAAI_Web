rule auto_rule_20250727002033_7934 {
  strings:
    $o0 = "dword_45CFC0" wide ascii nocase
    $o1 = "_setenvp" wide ascii nocase
    $o2 = "dword_45D3F4" wide ascii nocase
  condition:
    3 of ($o*)
}