rule auto_rule_20250727025359_7688 {
  strings:
    $o0 = "dword_43B53D" wide ascii nocase
    $o1 = "dword_43B5AE" wide ascii nocase
    $o2 = "dword_43B8D3" wide ascii nocase
    $o3 = "dword_43B6BD" wide ascii nocase
    $o4 = "dword_43B090" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727025402_5633 {
  strings:
    $o0 = "dword_43B72A" wide ascii nocase
    $o1 = "FindResourceA" wide ascii nocase
    $o2 = "x411EFD00u" wide ascii nocase
    $o3 = "dword_43B395" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250727025407_7066 {
  condition:
    auto_rule_20250727025359_7688 or auto_rule_20250727025402_5633
}