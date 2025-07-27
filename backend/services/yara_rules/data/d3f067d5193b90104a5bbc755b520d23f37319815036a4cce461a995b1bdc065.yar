rule auto_rule_20250727002854_5347 {
  strings:
    $o0 = "dword_46442C" wide ascii nocase
    $o1 = "xC0000092" wide ascii nocase
    $o2 = "_itoa" wide ascii nocase
  condition:
    3 of ($o*)
}