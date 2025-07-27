rule auto_rule_20250727015514_5918 {
  strings:
    $o0 = "dword_45DD88" wide ascii nocase
    $o1 = "StringTypeW" wide ascii nocase
    $o2 = "dword_45DEEC" wide ascii nocase
  condition:
    3 of ($o*)
}