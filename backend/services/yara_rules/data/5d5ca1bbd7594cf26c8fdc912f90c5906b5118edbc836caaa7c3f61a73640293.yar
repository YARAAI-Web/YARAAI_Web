rule auto_rule_20250727044337_7111 {
  strings:
    $o0 = "dword_43B05C" wide ascii nocase
    $o1 = "dword_43B82F" wide ascii nocase
    $o2 = "dword_43B223" wide ascii nocase
    $o3 = "dword_43B53D" wide ascii nocase
    $o4 = "dword_43B4DB" wide ascii nocase
  condition:
    4 of ($o*)
}