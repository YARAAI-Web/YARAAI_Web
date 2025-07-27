rule auto_rule_20250727004049_4569 {
  strings:
    $o0 = "dword_43B6F7" wide ascii nocase
    $o1 = "dword_43B3F2" wide ascii nocase
    $o2 = "dword_43B440" wide ascii nocase
    $o3 = "dword_43B40A" wide ascii nocase
    $o4 = "getsockopt" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727004053_2414 {
  strings:
    $o0 = "off_43B1CA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727004057_3652 {
  condition:
    auto_rule_20250727004049_4569 or auto_rule_20250727004053_2414
}