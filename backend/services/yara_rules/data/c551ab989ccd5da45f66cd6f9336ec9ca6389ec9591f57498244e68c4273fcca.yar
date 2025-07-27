rule auto_rule_20250726232247_0644 {
  strings:
    $o0 = "x6EC3500u" wide ascii nocase
    $o1 = "dword_43B30A" wide ascii nocase
    $o2 = "x7A468900" wide ascii nocase
    $o3 = "dword_43B0AB" wide ascii nocase
    $o4 = "dword_43B681" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726232250_6294 {
  strings:
    $o0 = "dword_43B48B" wide ascii nocase
    $o1 = "dword_43B1F5" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726232254_0685 {
  condition:
    auto_rule_20250726232247_0644 or auto_rule_20250726232250_6294
}