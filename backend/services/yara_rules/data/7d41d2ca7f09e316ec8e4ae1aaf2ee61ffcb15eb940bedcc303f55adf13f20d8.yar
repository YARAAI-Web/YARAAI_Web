rule auto_rule_20250726085024_0828 {
  strings:
    $o0 = "x10328E51" wide ascii nocase
    $o1 = "dword_42E6ED" wide ascii nocase
    $o2 = "xF0Fu" wide ascii nocase
    $o3 = "off_42E7FD" wide ascii nocase
    $o4 = "XAmount" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726085027_5464 {
  strings:
    $o0 = "xC2853B8C" wide ascii nocase
    $o1 = "lprect" wide ascii nocase
    $o2 = "x711D" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726085031_4554 {
  condition:
    auto_rule_20250726085024_0828 or auto_rule_20250726085027_5464
}