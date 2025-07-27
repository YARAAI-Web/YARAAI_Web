rule auto_rule_20250726222127_6783 {
  strings:
    $o0 = "xFFFFFF" wide ascii nocase
    $o1 = "dword_470668" wide ascii nocase
    $o2 = "dword_43A1F0" wide ascii nocase
  condition:
    3 of ($o*)
}