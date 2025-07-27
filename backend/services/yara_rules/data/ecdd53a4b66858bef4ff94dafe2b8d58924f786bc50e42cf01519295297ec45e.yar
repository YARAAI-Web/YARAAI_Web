rule auto_rule_20250726233421_9695 {
  strings:
    $o0 = "kr1C4_4" wide ascii nocase
    $o1 = "kr14C_4" wide ascii nocase
    $o2 = "kr2E4_4" wide ascii nocase
    $o3 = "kr1D0_4" wide ascii nocase
    $o4 = "kr1CC_4" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726233425_2476 {
  strings:
    $o0 = "krE0_4" wide ascii nocase
    $o1 = "kr1B8_4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726233428_5862 {
  condition:
    auto_rule_20250726233421_9695 or auto_rule_20250726233425_2476
}