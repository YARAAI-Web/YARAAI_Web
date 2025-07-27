rule auto_rule_20250726071633_5085 {
  strings:
    $o0 = "InitializeCriticalSec" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "_abnormal_termination" wide ascii nocase
    $o3 = "dword_45CB00" wide ascii nocase
  condition:
    4 of ($o*)
}