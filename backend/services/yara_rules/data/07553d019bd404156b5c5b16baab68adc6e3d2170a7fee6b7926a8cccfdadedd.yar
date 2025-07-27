rule auto_rule_20250727014641_9451 {
  strings:
    $o0 = "UsedDefaultChar" wide ascii nocase
    $o1 = "x4028D0" wide ascii nocase
    $o2 = "_CrtMemCheckpoint" wide ascii nocase
    $o3 = "Object" wide ascii nocase
    $o4 = "Handler" wide ascii nocase
  condition:
    4 of ($o*)
}