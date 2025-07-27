rule auto_rule_20250727043838_6773 {
  strings:
    $o0 = "dword_1011D6F0" wide ascii nocase
    $o1 = "cef_base64encode" wide ascii nocase
    $o2 = "dword_1011D718" wide ascii nocase
    $o3 = "StartFragment" wide ascii nocase
  condition:
    4 of ($o*)
}