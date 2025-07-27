rule auto_rule_20250727015833_5143 {
  strings:
    $o0 = "aQnpzuzufsqik" wide ascii nocase
    $o1 = "dword_43B4CF" wide ascii nocase
    $o2 = "dword_43B63F" wide ascii nocase
    $o3 = "dword_43B0A5" wide ascii nocase
    $o4 = "dword_43B162" wide ascii nocase
  condition:
    4 of ($o*)
}