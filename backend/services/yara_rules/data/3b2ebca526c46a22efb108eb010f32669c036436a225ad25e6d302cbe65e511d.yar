rule auto_rule_20250726191414_9550 {
  strings:
    $o0 = "dword_42E6ED" wide ascii nocase
    $o1 = "x8FEC9A90B92BA8A3uLL" wide ascii nocase
    $o2 = "dword_42E871" wide ascii nocase
    $o3 = "x28000001184LL" wide ascii nocase
    $o4 = "off_42E8F1" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726191417_5703 {
  strings:
    $o0 = "x30CEu" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726191421_1312 {
  condition:
    auto_rule_20250726191414_9550 or auto_rule_20250726191417_5703
}