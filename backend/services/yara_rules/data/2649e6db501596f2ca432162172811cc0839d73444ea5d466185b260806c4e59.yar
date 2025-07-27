rule auto_rule_20250726175527_0511 {
  strings:
    $o0 = "lphl" wide ascii nocase
    $o1 = "piIcon" wide ascii nocase
    $o2 = "CreateWaitableTimerW" wide ascii nocase
    $o3 = "GetCommProperties" wide ascii nocase
    $o4 = "x41000u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726175531_9533 {
  strings:
    $o0 = "lpClipRect" wide ascii nocase
    $o1 = "nIconIndex" wide ascii nocase
    $o2 = "propIndex" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726175532_0035 {
  condition:
    auto_rule_20250726175527_0511 or auto_rule_20250726175531_9533
}