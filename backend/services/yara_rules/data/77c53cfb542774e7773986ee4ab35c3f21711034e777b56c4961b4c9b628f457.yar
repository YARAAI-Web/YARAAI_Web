rule auto_rule_20250727042918_4021 {
  strings:
    $o0 = "dword_43B8AE" wide ascii nocase
    $o1 = "dword_43B2C5" wide ascii nocase
    $o2 = "dword_43B414" wide ascii nocase
    $o3 = "dword_43B7BF" wide ascii nocase
    $o4 = "dword_43B855" wide ascii nocase
  condition:
    4 of ($o*)
}