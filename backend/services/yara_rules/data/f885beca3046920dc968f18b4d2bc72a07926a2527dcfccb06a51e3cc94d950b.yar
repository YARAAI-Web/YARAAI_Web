rule auto_rule_20250726153302_5600 {
  strings:
    $o0 = "objects" wide ascii nocase
    $o1 = "stru_4603E0" wide ascii nocase
    $o2 = "_heap_init" wide ascii nocase
    $o3 = "_flushall" wide ascii nocase
  condition:
    4 of ($o*)
}