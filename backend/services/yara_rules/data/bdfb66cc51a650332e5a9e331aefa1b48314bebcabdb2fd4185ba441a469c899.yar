rule auto_rule_20250726135312_6108 {
  strings:
    $o0 = "byte_46DF60" wide ascii nocase
    $o1 = "InitializeCriticalSec" wide ascii nocase
    $o2 = "_SEH_epilog" wide ascii nocase
    $o3 = "lppf" wide ascii nocase
    $o4 = "x12010u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726135315_1956 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "UnwindUp5_0" wide ascii nocase
    $o2 = "dword_46DF30" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726135320_9938 {
  condition:
    auto_rule_20250726135312_6108 or auto_rule_20250726135315_1956
}