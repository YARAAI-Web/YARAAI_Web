rule auto_rule_20250726122429_3088 {
  strings:
    $o0 = "dword_43B542" wide ascii nocase
    $o1 = "dword_43B3B7" wide ascii nocase
    $o2 = "dword_43B53D" wide ascii nocase
    $o3 = "dword_43B4B7" wide ascii nocase
    $o4 = "dword_43B775" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726122432_1848 {
  strings:
    $o0 = "aQnpzuzufsqik" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726122437_1743 {
  condition:
    auto_rule_20250726122429_3088 or auto_rule_20250726122432_1848
}