rule auto_rule_20250726203453_8846 {
  strings:
    $o0 = "TrailUp0_0" wide ascii nocase
    $o1 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o2 = "nBlockUse" wide ascii nocase
  condition:
    3 of ($o*)
}