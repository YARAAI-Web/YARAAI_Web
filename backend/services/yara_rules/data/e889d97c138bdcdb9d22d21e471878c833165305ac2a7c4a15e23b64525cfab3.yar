rule auto_rule_20250726165447_6566 {
  strings:
    $o0 = "x299" wide ascii nocase
    $o1 = "x37A2FFFF862ALL" wide ascii nocase
    $o2 = "x4E790000174CLL" wide ascii nocase
    $o3 = "dword_422972" wide ascii nocase
    $o4 = "off_422268" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726165450_6557 {
  strings:
    $o0 = "dword_422952" wide ascii nocase
    $o1 = "dword_4228B2" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726165455_4563 {
  condition:
    auto_rule_20250726165447_6566 or auto_rule_20250726165450_6557
}