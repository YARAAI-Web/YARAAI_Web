rule auto_rule_20250726221231_4216 {
  strings:
    $o0 = "x4C58u" wide ascii nocase
    $o1 = "dword_42967C" wide ascii nocase
    $o2 = "x13C2000079BCLL" wide ascii nocase
    $o3 = "dword_42956C" wide ascii nocase
    $o4 = "dword_429698" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726221234_2653 {
  strings:
    $o0 = "dword_429660" wide ascii nocase
    $o1 = "dword_429684" wide ascii nocase
    $o2 = "dword_4298B9" wide ascii nocase
    $o3 = "x49E200003162LL" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726221236_0058 {
  condition:
    auto_rule_20250726221231_4216 or auto_rule_20250726221234_2653
}