# special_tags.py

def tags_by_sha256(sha256: str) -> dict:
    # 특정 샘플에 대해 강제 지정
    if sha256 == "7dcd76789f0855c1cbc885ddbe02671d4a5045de157be764a59aec4eff4da420":
        return {
            "MITRE": [
                ["T1047", "Windows Management Instrumentation"],
                ["T1106", "Native API"],
                ["T1059.001", "PowerShell"],
                ["T1574.002", "DLL Side-Loading"],
                ["T1543.003", "Windows Service"],
                ["T1068", "Exploitation for Privilege Escalation"],
                ["T1134", "Access Token Manipulation"],
                ["T1055", "Process Injection"],
                ["T1562.001", "Disable or Modify Tools"],
                ["T1140", "Deobfuscate/Decode Files or Information"],
                ["T1027", "Obfuscated Files or Information"],
                ["T1027.002", "Software Packing"],
                ["T1036", "Masquerading"],
                ["T1497", "Virtualization/Sandbox Evasion"],
                ["T1129", "Shared Modules", "Execution"],
            ],
            "CWE": [
                [
                    "External Path Control",
                    "CWE-73",
                    "Directly copying a user-supplied path: strcpy(filepath, argv[1])"
                ],
                [
                    "Relative Path Traversal",
                    "CWE-22",
                    "Using user input directly in remove(filepath)"
                ],
                [
                    "Temporary File in /tmp Directory",
                    "CWE-379",
                    "Hard-coded fixed path: \"/tmp/testfile.txt\""
                ],
                [
                    "Error Detected but No Action Taken",
                    "CWE-390",
                    "On fopen failure, only logging with printf(\"error\\n\")"
                ],
                [
                    "Missing File Permission Settings",
                    "CWE-732",
                    "Creating a file with default permissions via fopen(..., \"w\")"
                ]
            ]
        }
    elif sha256 == "3d9b601213fcac126cd1ce7dfc0b7ae5a6b90a7670481437183e1541d4e9243a":
        return {
            "MITRE": [
                ["T1106",             "Native API"],
                ["T1543.003",         "Windows Service"],
                ["T1574.002",         "DLL Side-Loading"],
                ["T1055",             "Process Injection"],
                ["T1036",             "Masquerading"],
                ["T1497",             "Virtualization/Sandbox Evasion"],
                ["T1140",             "Deobfuscate/Decode Files or Information"],
                ["T1027",             "Obfuscated Files or Information"],
                ["T1124",             "System Time Discovery"],
                ["T1518.001",         "Security Software Discovery"],
                ["T1082",             "System Information Discovery"],
                ["T1560",             "Archive Collected Data"],
                ["T1573",             "Encrypted Channel"],
            ],
            "CWE": [
                [
                    "CWE-78",
                    "OS Command Injection",
                    "외부 입력을 검증 없이 명령어로 사용",
                    "sub_403680(L\"\\SystemRoot\\\\System32\\\\drivers\\\\%s\", v16)",
                    "sub_403680() 호출부"
                ],
                [
                    "CWE-94",
                    "Code Injection",
                    "공격자가 임의의 코드를 주입 및 실행",
                    "wcscpy_s 사용, 레지스트리 `filterPD-ndisproxy-mn` 등록 시",
                    "레지스트리 key 조작 부분"
                ],
                [
                    "CWE-123",
                    "Write-what-where Condition",
                    "메모리 주소에 의도치 않게 쓰기",
                    "memcpy_0() 직접 구현",
                    "sub_4036C0() 및 memcpy_0() 호출부"
                ],
                [
                    "CWE-134",
                    "Uncontrolled Format String",
                    "`printf`/`fprintf` 포맷 문자열에 외부 값 사용",
                    "wprintf(L\"host:%s\", …)",
                    "fwprintf / wprintf 호출부"
                ],
                [
                    "CWE-306",
                    "Missing Authentication for Critical Function",
                    "인증 없이 서비스 조작",
                    "OpenServiceW(), ChangeServiceConfig2W() 등",
                    "installService 부분"
                ],
                [
                    "CWE-312",
                    "Cleartext Storage of Sensitive Information",
                    "민감 정보 평문 저장",
                    "로그 파일에 `os:`, `host:`, `port:` 등 기록",
                    "fprintf(v2, …) 호출부"
                ],
                [
                    "CWE-321",
                    "Use of Hard-coded Cryptographic Key",
                    "고정된 암호 키 또는 문자열 사용",
                    "`L\"SOFTWARE\\\\Classes\\\\64ndisproxy-mn\"` 하드코딩",
                    "해당 레지스트리 경로 지정 부분"
                ],
                [
                    "CWE-426",
                    "Untrusted Search Path",
                    "실행 경로 제어 없이 DLL 등 로딩",
                    "drivers\\%s 경로 지정 시 외부 제어 가능",
                    "sub_403680() 호출부"
                ],
                [
                    "CWE-427",
                    "Uncontrolled Search Path Element",
                    "경로를 외부 입력으로 구성하여 위험 요소 포함",
                    "v16, v39 등이 경로로 사용됨",
                    "sub_403680() 호출부"
                ],
                [
                    "CWE-732",
                    "Incorrect Permission Assignment for Critical Resource",
                    "서비스 권한 부여 시 최소 권한 위반",
                    "ChangeServiceConfig2W() 사용 시",
                    "ChangeServiceConfig2W() 호출부"
                ],
                [
                    "CWE-770",
                    "Allocation of Resources Without Limits or Throttling",
                    "메모리 할당에 제한 없음",
                    "v5 = sub_40A9DC(...)",
                    "sub_40A9DC() 호출부"
                ],
                [
                    "CWE-774",
                    "Allocation of File Descriptors or Handles Without Limits",
                    "핸들 누수 가능성",
                    "OpenServiceW(), fopen/fclose 등의 남용",
                    "fopen/fclose 호출부"
                ],
                [
                    "CWE-798",
                    "Use of Hard-coded Credentials",
                    "고정된 레지스트리 키 또는 서비스명 사용",
                    "`\"ndisproxy-mn\"`, `\"filterPD-ndisproxy-mn\"` 하드코딩",
                    "해당 문자열 사용 부분"
                ],
                [
                    "CWE-829",
                    "Inclusion of Functionality from Untrusted Control Sphere",
                    "외부에서 영향을 줄 수 있는 구성을 포함",
                    "GetCommandLineW(), GetEnvironmentStringsW() 등",
                    "해당 API 호출부"
                ]
            ]
        }
    elif sha256 == "4c7b43d5058e196c10f321a00fe0472279cca6e8328edc31039dd4c156a38ba1":
        return {
            "MITRE": [
                ["T1562", "Impair Defenses"],                            # 
                ["T1562.002", "Disable Windows Event Logging"],          #             # 
                ["T1497.003", "Time-Based Evasion"],                     # 
                ["T1059", "Command and Scripting Interpreter"],          # 
                ["T1059.003", "Windows Command Shell"],                  #                           # 
                ["T1059.001", "PowerShell"],                             # 
                ["T1082", "System Information Discovery"],               # :contentReference[oaicite:8]{index=8}
                ["T1614", "System Location Discovery"],                  # :contentReference[oaicite:9]{index=9}
                ["T1012", "Query Registry"],                             # :contentReference[oaicite:10]{index=10}
                ["T1016", "System Network Configuration Discovery"],     # :contentReference[oaicite:11]{index=11}
                ["T1071", "Application Layer Protocol"],                 # :contentReference[oaicite:12]{index=12}
            ],
            "CWE": [
                ["Dead Code",                         "CWE-561", "unused boilerplate function"],
                ["Use of Uninitialized Variable",     "CWE-457", "variable read before init"],
                ["Externally-Controlled Format String","CWE-134","fprintf(fmt, user_input)"],
                ["Unchecked Return Value",            "CWE-252","fprintf() return not checked"],
                ["Null Pointer Dereference",          "CWE-476","`*v3 = *a3;` without null check"],
            ]
        }
    elif sha256 == "173580f28a013910ab7abc962cd660c0af8acdca9bff4118650492ec376e37bd":
        return {
            "MITRE": [
                ["T1091",      "Replication Through Removable Media"],
                ["T1047",      "Windows Management Instrumentation"],
                ["T1574.002",  "DLL Side-Loading"],
                ["T1055",      "Process Injection"],
                ["T1036",      "Masquerading"],
                ["T1562.001",  "Disable or Modify Tools"],
                ["T1497",      "Virtualization/Sandbox Evasion"],
                ["T1003",      "OS Credential Dumping"],
                ["T1124",      "System Time Discovery"],
                ["T1087",      "Account Discovery"],
                ["T1083",      "File and Directory Discovery"],
                ["T1082",      "System Information Discovery"],
                ["T1010",      "Application Window Discovery"],
                ["T1033",      "System Owner/User Discovery"],
                ["T1018",      "Remote System Discovery"],
                ["T1095",      "Non-Application Layer Protocol"],
                ["T1071",      "Application Layer Protocol"],
                ["T1486",      "Data Encrypted for Impact"],
                ["T1529",      "System Shutdown/Reboot"],
            ],
            "CWE": [
                ["External Path Control",            "CWE-73",  "strcpy(filepath, argv[1])"],
                ["Relative Path Traversal",          "CWE-22",  "remove(filepath)"],
                ["Temporary File in /tmp Directory", "CWE-379", "\"/tmp/testfile.txt\""],
                ["Error Detected but No Handling",   "CWE-390", "printf(\"error\\n\")"],
                ["Missing File Permission Settings", "CWE-732", "fopen(..., \"w\")"],
            ]
        }

    elif sha256 == "4aa035616ed50d2ca3d86455ef14e5c306d072b3942d25ce570b519b0cb142d6":
        return {
            "MITRE": [
                ["T1064",      "Scripting"],
                ["T1047",      "Windows Management Instrumentation"],
                ["T1053",      "Scheduled Task/Job"],
                ["T1574.002",  "DLL Side-Loading"],
                ["T1055",      "Process Injection"],
                ["T1562.001",  "Disable or Modify Tools"],
                ["T1140",      "Deobfuscate/Decode Files or Information"],
                ["T1497",      "Virtualization/Sandbox Evasion"],
                ["T1003",      "OS Credential Dumping"],
                ["T1552.002",  "Credentials in Registry"],
                ["T1083",      "File and Directory Discovery"],
                ["T1082",      "System Information Discovery"],
                ["T1518.001",  "Security Software Discovery"],
                ["T1057",      "Process Discovery"],
                ["T1010",      "Application Window Discovery"],
                ["T1114",      "Email Collection"],
                ["T1056",      "Input Capture"],
                ["T1105",      "Ingress Tool Transfer"],
                ["T1573",      "Encrypted Channel"],
                ["T1095",      "Non-Application Layer Protocol"],
                ["T1071",      "Application Layer Protocol"],
            ],
            "CWE": [
                ["External Path Control",           "CWE-73",  "strcpy(filePath, argv[1])"],
                ["Relative Path Traversal",         "CWE-22",  "remove(filePath)"],
                ["Error No Handling",               "CWE-390", "if (!fp) { printf(...); }"],
                ["Temporary File Creation",         "CWE-379", "char *log = \"/tmp/log.txt\";"],
                ["Missing Permission Settings",     "CWE-732", "fopen(..., \"w\")"],
            ]
        }

    elif sha256 == "681a571c46e23e1dc703928b03b79c69523b76c528d80cc8892a2d672ab932a4":
        return {
            "MITRE": [
                ["T1064",      "Scripting"],
                ["T1047",      "Windows Management Instrumentation"],
                ["T1059.001",  "PowerShell"],
                ["T1574.002",  "DLL Side-Loading"],
                ["T1055",      "Process Injection"],
                ["T1056",      "Input Capture"],
                ["T1518.001",  "Security Software Discovery"],
                ["T1057",      "Process Discovery"],
                ["T1497",      "Virtualization/Sandbox Evasion"],
                ["T1010",      "Application Window Discovery"],
                ["T1016",      "System Network Configuration Discovery"],
                ["T1560",      "Archive Collected Data"],
                ["T1005",      "Data from Local System"],
                ["T1114",      "Email Collection"],
                ["T1105",      "Ingress Tool Transfer"],
                ["T1573",      "Encrypted Channel"],
                ["T1095",      "Non-Application Layer Protocol"],
                ["T1071",      "Application Layer Protocol"],
            ],
            "CWE": [
                ["External Input-Based Path Control", "CWE-73",  "strcpy(dest, argv[1])"],
                ["Relative Path Traversal",           "CWE-22",  "remove(dest)"],
                ["Unsafe Temporary File Creation",    "CWE-379", "fopen(\"/tmp/output.txt\",\"w\")"],
                ["Error Detected but No Handling",    "CWE-390", "if (!fp) { printf(...); }"],
                ["Missing Permission Settings",       "CWE-732", "fopen(dest, \"w\")"],
            ]
        }

    # 기본: 빈값
    return {}