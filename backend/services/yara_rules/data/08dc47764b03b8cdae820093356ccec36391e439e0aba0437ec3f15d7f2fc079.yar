rule auto_rule_20250726193744_8489 {
  strings:
    $o0 = "dword_45DEF4" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
    $o2 = "LockFile" wide ascii nocase
    $o3 = "__freetlocinfo" wide ascii nocase
    $o4 = "InitializeCriticalSec" wide ascii nocase
  condition:
    5 of ($o*)
}